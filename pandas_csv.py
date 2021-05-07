import pandas as pd

# * read csv
df = pd.read_csv("assets/pokemon.csv")

# * get columns
df.columns

# * get first 5 rows
df.head(5)

# * get last 5 rows
df.tail(5)

# * print where generation = 1 and type = grass
print(df.loc[
    (df['Generation'] == 1) &
    ((df['Type 1'] == "Grass") | (df['Type 2'] == "Grass"))
])
