import pandas as pd

revenue = pd.read_csv("data/Exercise KPIs for students - Barcelona.csv")

revenue = revenue.iloc[2:,3:]

print(revenue)

