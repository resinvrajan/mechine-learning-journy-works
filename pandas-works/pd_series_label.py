import pandas as pd
salery=[30000,34000,35000,36000]
series=pd.Series(salery)
print(series)
print(series[1])
print(series[0])
print(series[1:3])
# changing index
series=pd.Series(salery,index=["e1","e2","e3","e4"])
print(series)
print(series["e1"])
print(series["e1":"e4"])