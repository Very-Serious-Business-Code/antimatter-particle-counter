import pandas as pd

query = str(input("Antimater partical chart? "))
df = pd.read_excel(str(query), index_col=0)
print(df)
