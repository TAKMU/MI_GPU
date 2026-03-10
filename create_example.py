import pandas as pd

df = pd.read_csv("data/example.tsv", sep="\t", index_col=0)
df.head(100).to_csv("data/example.tsv", sep="\t", index=True)