import pandas as pd

pokemon_data = pd.read_excel("data/pokemon_data.xlsx")

print(pokemon_data.tail(3))