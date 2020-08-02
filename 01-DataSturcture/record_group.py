'''
File: record_group.py
Project: 01-DataSturcture
===========
File Created: Tuesday, 21st July 2020 3:23:53 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Tuesday, 21st July 2020 3:23:57 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 记录分组
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from operator import itemgetter
from itertools import groupby


# 创建记录
records = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 先按照给定字段将数据排序
records.sort(key=itemgetter('date'))

# 分组，一次迭代查找连续的相同值，返回一个值和一个迭代器对象
for date, items in groupby(records, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 扩展，可以将分组结果存到字典中
