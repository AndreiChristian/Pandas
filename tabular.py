import pandas as pd

# titanic = pd.read_csv('data/titanic_data.csv')

# print(titanic.tail())

# print(titanic.dtypes)

# titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

print(titanic.info())