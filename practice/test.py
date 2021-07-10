import pandas as pd

fruitData = {'fruitName':['apple','banana','cherry','pear'],
             'fruitPrice':[2500,3800,6000,1200],
             'num':[10,5,3,8]}

df = (pd.DataFrame(fruitData, columns=['fruitName', 'fruitPrice', 'num']))
print(df)
df.to_csv('test.csv')