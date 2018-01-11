# encoding=utf-8

"""
# Assuming file has following 5 lines
131071
131072
131073
131074
131075

"""

with open('131071.txt', mode='r+') as file:
    print(file.readlines())
    file.seek(0, 0)  # 改变位置指针
    print(file.tell())  # 打印指针位置
    file.writelines(['hello\n', 'world'])
    file.write('haha\n')
    print('============')
    p1 = file.read(6)

    p2 = file.read()
    print(p1)
    print(p2)

import sys

sys.stdout.write('helloworld!\n')
sys.stderr.write('helloworld!\n')
sys.stdin.write('helloworld!\n')
