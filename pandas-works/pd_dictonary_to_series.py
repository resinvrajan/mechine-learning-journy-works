import pandas as pd
student_total={"s1":450,"s2":475,"s3":490,"s4":485}
series=pd.Series(student_total)
print(series)
print(series["s4"])

# create a employee dictionary and convert that to series

employee={"e1":10,"e2":20,"e3":30,"e4":40}
series1=pd.Series(employee)
print(series1)


# agregate functions
# max()
# min()
# sum()
# mean()
print(series.sum())
print(series.max())
print(series.min())
print(series.mean())