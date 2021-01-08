'''
File: anyobj_sort.py
Project: 01-DataSturcture
===========
File Created: Tuesday, 21st July 2020 3:16:28 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Tuesday, 21st July 2020 3:16:32 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 使对象支持排序
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from operator import attrgetter


# 要排序的类
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23, 'aa'), User(3, 'aa'), User(99, 'bb')]

# 单属性的排序
print(sorted(users, key=attrgetter('user_id')))

# 多属性的排序
print(sorted(users, key=attrgetter('name', 'user_id')))

# 最小值
a = min(users, key=attrgetter('user_id'))
print(a.user_id, a.name)

# 最大值
print(max(users, key=attrgetter('user_id')))
