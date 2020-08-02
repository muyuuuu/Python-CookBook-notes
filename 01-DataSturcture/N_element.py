'''
File: N_element.py
Project: DataSturcture
===========
File Created: Monday, 20th July 2020 11:08:11 am
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 11:44:06 am
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 保留序列中 N 个元素的问题
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

import heapq
from collections import deque

# 保留最后 N 个元素
# 先入先出
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(6)
print(q)

# 队首插入
q.appendleft(4)
print(q)

# 队尾弹出
a = q.pop()
print(a, q)

# 队首弹出
b = q.popleft()
print(b, q)


# 查找最大或最小的 N 个元素
nums = [1, 2, 3, 4, 5, 6, 6, 6, 1, 1]
print(heapq.nlargest(3, nums)) 
print(heapq.nsmallest(3, nums)) 


# 更复杂的数据结构
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# 会打印全部记录
print(cheap)
print(expensive)

# 当 N 和集合大小差不多时，建议排序后切片
