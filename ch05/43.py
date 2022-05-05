class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs    
        self.dst = dst          
        self.srcs = []      


def parse_cabocha(block):
    def check_create_chunk(tmp):
        if len(tmp) > 0:
            c = Chunk(tmp, dst)
            res.append(c)
            tmp = []
        return tmp

    res = []
    tmp = []
    dst = None
    for line in block.split('\n'):
        if line == '':
            tmp = check_create_chunk(tmp)
        elif line[0] == '*':
            dst = line.split(' ')[2].rstrip('D')
            tmp = check_create_chunk(tmp)
        else:
            contents = line.split('\t')
            if len(contents) != 2: continue # EOSの排除
            surface = contents[0]
            attr = contents[1].split(',')
            lineDict = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1]
            }
            tmp.append(Morph(lineDict))

    for i, r in enumerate(res):
        res[int(r.dst)].srcs.append(i)
    return res


filename = 'ai.ja/ai.ja.txt.parsed'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_cabocha(block) for block in blocks]
for b in blocks:
    for m in b:
        pre_text = ''.join([mo.surface if mo.pos != '記号' else '' for mo in m.morphs])
        pre_pos = [mo.pos for mo in m.morphs]
        post_text = ''.join([mo.surface if mo.pos != '記号' else '' for mo in b[int(m.dst)].morphs])
        post_pos = [mo.pos for mo in b[int(m.dst)].morphs]
        if '名詞' in pre_pos and '動詞' in post_pos:
            print(pre_text, post_text, sep='\t')
