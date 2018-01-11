# encoding=utf-8

import requests

kw = dict(wd='费志辉')  # {'wd':'费志辉'}
r = requests.get('https://www.baidu.com/s', params=kw)

print(r.status_code)
print(r.text)
