'''
File: dict_merge.py
Project: 01-DataSturcture
===========
File Created: Tuesday, 21st July 2020 4:49:05 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Tuesday, 21st July 2020 4:49:09 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 字典合并
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from collections import ChainMap


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# 合并字典
# 在内部创建了一个容纳这些字典的列表
# 相同的键，只保留在第一个字典的
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(list(c.keys()))
print(list(c.values()))

# 所有的操作都只会影响第一个字典
c['z'] = 10
c['w'] = 20
print(a, b)

# 个人感觉 defaultdict 会好一些
