import pandas as pd
data=pd.read_csv("tasks\\task5\\malayalam_actors_actresses.csv")
print(data.shape)
print(data.head())
print(data.isnull().sum())
# count number of rows and columns
print(data.shape[0],"rows")
print(data.shape[1],"columns")
# place birth count
print(data["place_of_birth"].value_counts())
# male female count
print(data["gender"].value_counts())
# names
print(data["name"])
# year count
print(data["debut_year"].value_counts())
# most repeated year
print(data["debut_year"].value_counts().idxmax())
