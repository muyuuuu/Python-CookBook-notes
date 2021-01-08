'''
File: seq_filter.py
Project: 01-DataSturcture
===========
File Created: Tuesday, 21st July 2020 3:41:51 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Tuesday, 21st July 2020 3:41:55 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 过滤序列中的元素
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
import math
from itertools import compress


mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 列表推导，数据量大会浪费内存
a = [n if n > 0 else 0 for n in mylist]
print(a)

# 选择生成器
b = (math.pow(n, 2) for n in mylist if n > 0)
for i in b:
    print(i)


# 内置的 filter 函数, 解决复杂过滤
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try :
        int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)


# 按照一个序列对另一个序列筛选
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# 选出 counts 中元素大于 5 的地址
more5 = [n > 5 for n in counts]
a = compress(addresses, more5)
for rows in a:
    for item in rows:
        print(item, end='')
    print()
    # print(a)


# 过滤字典元素
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 价格过滤
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# 名称过滤
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = dict((key, value) for key, value in prices.items() if key in tech_names)
print(p2)
