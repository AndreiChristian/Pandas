import pandas as pd

df = pd.read_excel("data/pokemon_data.xlsx")

# reading columns

# print(df.columns)

# reading a specific column

# print(df['Name'])
# print(df[['Name','Type 1','HP']])

# reading a specific row

# print(df.iloc[1:4])

#reading from a specific location

print(df.iloc[2,1])
