import pandas as pd

titanic = pd.read_csv("data/titanic_data.csv")

# print(titanic['Age'].mean())

# print(titanic[['Age','Fare']].median())

print(titanic[['Sex','Age']].groupby("Sex").mean())