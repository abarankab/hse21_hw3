import pandas as pd

df = pd.read_csv("ALL.counts", sep="\t")
df = df.reindex(columns=["geneID", "c1", "c2", "c3", "r1", "r2", "r3"])
df.to_csv("ALL_1.counts", sep="\t", index=False)
print(df)