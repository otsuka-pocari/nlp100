import pandas as pd


df = pd.read_csv("popular-names.txt", sep="\t", header=None)
ans = df.sort_values(by=[2], ascending=False)
print(ans)
