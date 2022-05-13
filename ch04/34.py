def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
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
        res.append(lineDict)

def extract_noun_noun(block):
    res = []
    tmp = []
    for b in block:
        if b['pos'] == '名詞':
            tmp.append(b['surface'])
        elif len(tmp) >= 2:
            res.append(''.join(tmp))
            tmp = []
        else:
            tmp = []
    return res


filename = 'neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_mecab(block) for block in blocks]
ans = [extract_noun_noun(block) for block in blocks]
print(ans)
