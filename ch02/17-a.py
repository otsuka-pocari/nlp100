import pandas as pd

df = pd.read_csv("popular-names.txt", sep="\t", header=None)
ans = df[0]
ans = set(ans)
print(ans)
print("John"in ans)
