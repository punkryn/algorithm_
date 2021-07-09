import pandas as pd

##########데이터 로드

train_df = pd.DataFrame([
    [2, 1, 3],
    [3, 2, 5],
    [3, 4, 7],
    [5, 5, 10],
    [7, 5, 12],
    [2, 5, 7],
    [8, 9, 13],
    [9, 10, 13],
    [90, 100, 12], #이상값 추가
    [91, 101, 13], #이상값 추가
    [6, 12, 12]
], columns=['hour', 'attendance', 'score'])

test_df = pd.DataFrame([
    [9, 2, 13],
    [6, 10, 12],
    [2, 4, 6]
], columns=['hour', 'attendance', 'score'])

##########데이터 분석

##########데이터 전처리

quartile_1 = train_df.quantile(0.25)
quartile_3 = train_df.quantile(0.75)
IQR = quartile_3 - quartile_1
print('IQR')
print(IQR)
condition = (train_df < (quartile_1 - 1.5 * IQR)) | (train_df > (quartile_3 + 1.5 * IQR))
condition = condition.any(axis=1)
search_df = train_df[condition]
print('sdf')
print(search_df)
'''
   hour  attendance  score
8    90         100     12
9    91         101     13
'''

train_df = train_df.drop(search_df.index, axis=0)
print(train_df)
'''
    hour  attendance  score
0      2           1      3
1      3           2      5
2      3           4      7
3      5           5     10
4      7           5     12
5      2           5      7
6      8           9     13
7      9          10     13
10     6          12     12
'''
print(test_df)
'''
   hour  attendance  score
0     9           2     13
1     6          10     12
2     2           4      6
'''