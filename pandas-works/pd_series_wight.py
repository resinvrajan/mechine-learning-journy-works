import pandas as pd
weight=[65,50,74,54,67,76,59,64,66,77]
series=pd.Series(weight)
print(series)
print(series.head())   #this method prints the top 5 records
print(series.tail())   #this method prints the last 5 records
print(series.shape)  # its an atribute to show the row and column
