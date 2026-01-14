"""
pd.Series(data) is used to convert list to pandas series
"""

import pandas as pd
data=[165,163,167,170,164]
series=pd.Series(data)
print(series)
print(type(series))