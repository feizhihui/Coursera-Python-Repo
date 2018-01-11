# encoding=utf-8

#

import requests

id = '1291546'
# id = '1220562'
r = requests.get('https://api.douban.com/v2/movie/subject/' + id)

print(r.status_code)
# print(r.text)

data = r.json()  # dict
print(data['title'], data['rating']['average'])

r = requests.get('https://api.douban.com/v2/movie/subject/1292224')
# 1292720, 1292052, 1295644, 1291546
data = r.json()
print(data['title'], data['rating']['average'])
