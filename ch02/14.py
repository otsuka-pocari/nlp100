import pandas as pd


df = pd.read_csv("popular-names.txt", sep="\t", header=None)
get_row = df.head(5)

print(get_row)