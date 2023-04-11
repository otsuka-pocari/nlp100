from collections import defaultdict


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


def extract_words(block):
    return [b['base'] + '_' + b['pos'] + '_' + b['pos1'] for b in block]


filename = 'neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_mecab(block) for block in blocks]
words = [extract_words(block) for block in blocks]
d = defaultdict(int)
for word in words:
    for w in word:
        d[w] += 1
ans = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in range(100):
    print(ans[i])
