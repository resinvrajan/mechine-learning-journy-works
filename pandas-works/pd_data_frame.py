"""
data frame is like 2d array in numpy with rows and columns

"""



import pandas as pd
student={
    "name":["adhnan","adhil","risen","rafi","jibin"],
    "age":[23,24,25,26,25],
    "course":["ds","ds","dj","st","ds"]
}
df=pd.DataFrame(student)
print(df)
print(df[1:2])
print(df["course"])
print(df[["name","course","age"]])
print(df[["name","age"]])