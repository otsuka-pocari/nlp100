class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


def parse_cabocha(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        elif line[0] == '*':
            continue
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
        res.append(Morph(lineDict))


filename = 'ai.ja/ai.ja.txt.parsed'
with open(filename, mode='rt', encoding='utf-8',errors='ignore') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_cabocha(block) for block in blocks]
for m in blocks[2]:
    print(vars(m))
