import pandas as pd
ListOfData = pd.read_csv('IMVA2.csv')

num = 0
date = '1978 Feb'

del ListOfData[date]

ListOfData = ListOfData['1978 Jan'].str.split(' ', n=1, expand=True)
print(ListOfData)