'''
File: dict_calc.py
Project: 01-DataSturcture
===========
File Created: Monday, 20th July 2020 5:32:11 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 5:32:17 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 字典计算
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

# 字典计算，找最小值等
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'ABM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 按键排序
print(min(prices))
print(max(prices))

# 返回值和键
# 按照值排序
print(min(zip(prices.values(), prices.keys())))
# 按照键排序
print(max(zip(prices.keys(), prices.values())))


# 字典比较，交、并、补等
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 查找共同的键
print(a.keys() & b.keys())
# 键在 a，但不在 b
print(a.keys() - b.keys()) 
# 键值都相同
print(a.items() & b.items()) 


# 创建一个新字典
c = {key:a[key] for key in (a.keys() & b.keys()) - {'z', 'w'}}
print(c)


# 取字典元素的最小值
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)