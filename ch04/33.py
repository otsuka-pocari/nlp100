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

def extract_a_no_b(block):
    res = []
    for i in range(1, len(block) - 1):
        if block[i - 1]['pos'] == '名詞' and block[i]['base'] == 'の' and block[i + 1]['pos'] == '名詞':
            res.append(block[i - 1]['surface'] + block[i]['surface'] + block[i + 1]['surface'])
    return res

filename = 'neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_mecab(block) for block in blocks]
ans = [extract_a_no_b(block) for block in blocks]
print(ans)
