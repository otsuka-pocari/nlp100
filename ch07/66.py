from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

ws = []
with open('wordsim353/combined.csv', 'r') as f:
    next(f) # 1行目を飛ばす
    for line in f:
        line = [s.strip() for s in line.split(',')]
        line.append(model.similarity(line[0], line[1]))
        ws.append(line)


# スピアマン相関係数の計算
human = np.array(ws).T[2]
w2v = np.array(ws).T[3]
correlation, pvalue = spearmanr(human, w2v)

print(f'スピアマン相関係数: {correlation:.3f}')
