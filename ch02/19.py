import pandas as pd


df = pd.read_csv("popular-names.txt", sep="\t", header=None)
ans = df.value_counts(subset=[0], sort=True)
print(ans)
