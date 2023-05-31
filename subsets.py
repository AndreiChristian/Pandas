import pandas as pd

titanic_data = pd.read_excel("data/titanic.xlsx")

ages = titanic_data['Age']

# print(ages.shape)

# print(titanic_data[['Age','Sex']])

above_35 = titanic_data[titanic_data['Age']>35]

# print(above_35.shape)

# print(titanic_data[titanic_data['Pclass'].isin([2,3])])

# print(titanic_data[(titanic_data["Pclass"] == 2) | (titanic_data["Pclass"] == 3)])

age_no_na = titanic_data[titanic_data['Age'].notna()]

# print(age_no_na.shape)

adult_names = titanic_data.loc[titanic_data['Age']>35,'Name']

# print(adult_names)

print(titanic_data.iloc[9:25,2:5])