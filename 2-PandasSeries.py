import numpy as np
import pandas as pd

labels = ["a","b","c"]
my_list = [10,20,30]

arr = np.array([10,20,30])

d = {"a":10, "b":20,"c":100}

print_var = pd.Series(my_list,index = labels)

print(print_var)

print(pd.Series(d))

print(pd.Series(data=labels))

print(pd.Series([sum,print,len]))

ser1 = pd.Series([1,2,3,4],index=["USA","CHINA","FRANCE","GERMANY"])

ser2 = pd.Series([1,2,3,4],index=["USA","CHINA","ITALY","JAPAN"])

print(ser1["USA"])

print(ser2["JAPAN"])

print(ser1+ser2)
