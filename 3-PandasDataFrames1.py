import numpy as np
import pandas as pd

from numpy.random import randn

a = np.random.seed(101)


df = pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])

print(df)

print(df["W"])

print(df.W)
#Do not use this cuz its might be confusing with other methods

#multiple columns

print(df[["W","Z"]])

df["new"] = df["W"] + df["Y"]

print(df)

print(df.drop("new",axis=1))

df.drop("new",axis =1,inplace= True)

print(df)

print(df.drop("E",axis=0))

df.drop("E",axis=0,inplace=True)

print(df)

#ROW

print(df.loc["A"])

print(df.iloc[2])

print(df.loc["B","Y"])

print(df.loc[["A","B"],["W","Y"]])