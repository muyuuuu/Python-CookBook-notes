'''
File: named_slice.py
Project: 01-DataSturcture
===========
File Created: Monday, 20th July 2020 10:34:20 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 10:34:25 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 切片命名
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from collections import namedtuple


string = "00110022"
# 左开右闭
# 直接切片会导致代码可读性降低
a = slice(2, 4)
b = slice(6, 8)
print(int(string[a]) + int(string[b]))


# 访问切片对象
a = slice(1, 100, 2)
print(a.start, a.step, a.stop)


# 提前命名，并按名层访问序列
# 第一个参数是类名
Subscriber = namedtuple('people', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub.addr, sub.joined)


# 实例
records = [
    ['a', 12, 12],
    ['b', 12, 12],
    ['c', 12, 12],
    ['d', 12, 12],
    ['e', 12, 12],
]

Stock = namedtuple('record', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

print(compute_cost(records))


# 数据增加一列, 原函数不用修改，修改命名即可
records1 = [
    ['a', 12, 'test', 12],
    ['b', 12, 'test', 12],
    ['c', 12, 'test', 12],
    ['d', 12, 'test', 12],
    ['e', 12, 'test', 12],
]

Stock = namedtuple('Stock', ['name', 'shares', 'test', 'price'])
print(compute_cost(records1))
