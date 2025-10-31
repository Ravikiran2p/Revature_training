import pandas as pd

data=[1,2,3,4,5,]
print(data)
series=pd.Series(data)
print(series)

data={
    'name':['alice','bob','Charlie'],
    'age':[25,30,35],
    'city':['new york','san francisco','los angeles']
}

df=pd.DataFrame(data)
print(df)