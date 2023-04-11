import pandas as pd

df = pd.read_csv("popular-names.txt", sep="\t", header=None)
ans = df.replace("\t", " ")
print(ans)
