import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)

# print(df)

df.loc[df.AAA >=5,'BBB'] = -1

df.loc[df.AAA >=5,['BBB','CCC']] = 555

# print(df)

df_mask = pd.DataFrame({"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [True, False] * 2})

df.where(df_mask, -1000)

df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)

df['logic']= np.where(df['AAA']>5,"high","low")

print(df)