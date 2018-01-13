# encoding=utf-8

import pandas as pd

user = pd.read_csv('./ml-100k/ml-100k/u.user', sep='|', header=None)
user.columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
data = pd.read_csv('./ml-100k/ml-100k/u.data', sep='\t', header=None)
data.columns = ['user_id', 'item_id', 'rating', 'timestamp']
print(user.head())
print(data.head())

data = pd.merge(user, data, on='user_id')
print(data.head())

data = data.groupby(by='user_id').agg({'rating': 'mean', 'gender': 'all'})
print(data.head())
data = data.groupby(by='gender').agg({'rating': 'std'})
print(data)
