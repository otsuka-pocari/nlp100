from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib


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


def extract_base(block):
    return [b['base'] for b in block]


filename = 'neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_mecab(block) for block in blocks]
words = [extract_base(block) for block in blocks]
words = list(filter(lambda x: '猫' in x, words))
d = defaultdict(int)
for word in words:
    for w in word:
        if w != '猫':
            d[w] += 1
ans = sorted(d.items(), key=lambda x: x[1], reverse=True)[:10]
labels = [a[0] for a in ans]
values = [a[1] for a in ans]
plt.figure(figsize=(8, 8))
plt.barh(labels, values)
plt.savefig('ans37.png')
plt.show()
