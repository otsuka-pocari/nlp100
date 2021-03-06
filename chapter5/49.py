import CaboCha
import re

fname = 'neko.txt'
fname_parsed = 'neko.txt.cabocha'
fname_result = 'result.txt'


def parse_neko():
    '''「吾輩は猫である」を係り受け解析
    「吾輩は猫である」(neko.txt)を係り受け解析してneko.txt.cabochaに保存する
    '''
    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        cabocha = CaboCha.Parser()
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            )


class Morph:
    '''
    形態素クラス
    表層形（surface）、基本形（base）、品詞（pos）、品詞細分類1（pos1）を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    '''
    文節クラス
    形態素（Morphオブジェクト）のリスト（morphs）、係り先文節インデックス番号（dst）、
    係り元文節インデックス番号のリスト（srcs）をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        self.morphs = []
        self.srcs = []
        self.dst = -1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

    def normalized_surface(self):
        '''句読点などの記号を除いた表層形'''
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                result += morph.surface
        return result

    def chk_pos(self, pos):
        '''指定した品詞（pos）を含むかチェックする

        戻り値：
        品詞（pos）を含む場合はTrue
        '''
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_morphs_by_pos(self, pos, pos1=''):
        '''指定した品詞（pos）、品詞細分類1（pos1）の形態素のリストを返す
        pos1の指定がない場合はposのみで判定する

        戻り値：
        形態素（morph）のリスト、該当形態素がない場合は空のリスト
        '''
        if len(pos1) > 0:
            return [res for res in self.morphs
                    if (res.pos == pos) and (res.pos1 == pos1)]
        else:
            return [res for res in self.morphs if res.pos == pos]

    def get_kaku_prt(self):
        '''助詞を1つ返す
        複数ある場合は格助詞を優先し、最後の助詞を返す。

        戻り値：
        助詞、ない場合は空文字列
        '''
        prts = self.get_morphs_by_pos('助詞')
        if len(prts) > 1:

            # 2つ以上助詞がある場合は、格助詞を優先
            kaku_prts = self.get_morphs_by_pos('助詞', '格助詞')
            if len(kaku_prts) > 0:
                prts = kaku_prts

        if len(prts) > 0:
            return prts[-1].surface     # 最後を返す
        else:
            return ''

    def get_sahen_wo(self):
        '''「サ変接続名詞＋を」を含無場合は、その部分の表層形を返す

        戻り値：
        「サ変接続名詞＋を」の文字列、なければ空文字列
        '''
        for i, morph in enumerate(self.morphs[0:-1]):

            if (morph.pos == '名詞') \
                    and (morph.pos1 == 'サ変接続') \
                    and (self.morphs[i + 1].pos == '助詞') \
                    and (self.morphs[i + 1].surface == 'を'):
                return morph.surface + self.morphs[i + 1].surface

        return ''

    def noun_masked_surface(self, mask, dst=False):
        '''名詞を指定文字(mask)でマスクした表層形を返す
        dstがTrueの場合は最左の名詞をマスクした以降は切り捨てて返す

        戻り値：
        名詞をマスクした表層形
        '''
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                if morph.pos == '名詞':
                    result += mask
                    if dst:
                        return result
                    mask = ''       # 最初に見つけた名詞をマスク、以降の名詞は除去
                else:
                    result += morph.surface
        return result


def neco_lines():
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで、
    1文ずつChunkクラスのリストを返す

    戻り値：
    1文のChunkクラスのリスト
    '''
    with open(fname_parsed) as file_parsed:

        chunks = dict()     # idxをkeyにChunkを格納
        idx = -1

        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':

                # Chunkのリストを返す
                if len(chunks) > 0:

                    # chunksをkeyでソートし、valueのみ取り出し
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_tuple))[1]
                    chunks.clear()

                else:
                    yield []

            # 先頭が*の行は係り受け解析結果なので、Chunkを作成
            elif line[0] == '*':

                # Chunkのインデックス番号と係り先のインデックス番号取得
                cols = line.split(' ')
                idx = int(cols[1])
                dst = int(re.search(r'(.*?)D', cols[2]).group(1))

                # Chunkを生成（なければ）し、係り先のインデックス番号セット
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先のChunkを生成（なければ）し、係り元インデックス番号追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # それ以外の行は形態素解析結果なので、Morphを作りChunkに追加
            else:

                # 表層形はtab区切り、それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph作成、リストに追加
                chunks[idx].morphs.append(
                    Morph(
                        cols[0],        # surface
                        res_cols[6],    # base
                        res_cols[0],    # pos
                        res_cols[1]     # pos1
                    )
                )

        raise StopIteration


# 係り受け解析
parse_neko()

# 結果ファイル作成
with open(fname_result, mode='w') as out_file:

    # 1文ずつリスト作成
    for chunks in neco_lines():

        # 名詞を含むchunkに限定した、chunksにおけるインデックスのリストを作成
        indexs_noun = [i for i in range(len(chunks))
                if len(chunks[i].get_morphs_by_pos('名詞')) > 0]

        # 2つ以上ある？
        if len(indexs_noun) < 2:
            continue

        # 名詞を含むchunkの組み合わせを総当りでチェック
        for i, index_x in enumerate(indexs_noun[:-1]):
            for index_y in indexs_noun[i + 1:]:

                meet_y = False          # Yにぶつかった？
                index_dup = -1          # XとYの経路がぶつかったchunkのindex
                routes_x = set()        # Xの経路チェック用

                # 名詞Xから根に向かって、Yにぶつからないか調べながら探索
                dst = chunks[index_x].dst
                while dst != -1:
                    if dst == index_y:
                        meet_y = True           # Yにぶつかった
                        break
                    routes_x.add(dst)           # 経路チェックのために保存
                    dst = chunks[dst].dst

                # 名詞Yから根まで、Xの経路にぶつからないか調べながら探索
                if not meet_y:
                    dst = chunks[index_y].dst
                    while dst != -1:
                        if dst in routes_x:
                            index_dup = dst     # Xの経路とぶつかった
                            break
                        else:
                            dst = chunks[dst].dst

                # 結果出力
                if index_dup == -1:

                    # XからYにぶつかるパターン
                    out_file.write(chunks[index_x].noun_masked_surface('X'))
                    dst = chunks[index_x].dst
                    while dst != -1:
                        if dst == index_y:
                            out_file.write(
                                    ' -> ' + chunks[dst].noun_masked_surface('Y', True))
                            break
                        else:
                            out_file.write(
                                    ' -> ' + chunks[dst].normalized_surface())
                        dst = chunks[dst].dst
                    out_file.write('\n')

                else:

                    # 経路上の共通のchunkでぶつかるパターン

                    # Xからぶつかる手前までを出力
                    out_file.write(chunks[index_x].noun_masked_surface('X'))
                    dst = chunks[index_x].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + chunks[dst].normalized_surface())
                        dst = chunks[dst].dst
                    out_file.write(' | ')

                    # Yからぶつかる手前までを出力
                    out_file.write(chunks[index_y].noun_masked_surface('Y'))
                    dst = chunks[index_y].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + chunks[dst].normalized_surface())
                        dst = chunks[dst].dst
                    out_file.write(' | ')

                    # ぶつかったchunkを出力
                    out_file.write(chunks[index_dup].normalized_surface())
                    out_file.write('\n')
