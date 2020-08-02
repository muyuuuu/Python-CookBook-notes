'''
File: dict_add_element.py
Project: DataSturcture
===========
File Created: Monday, 20th July 2020 12:17:31 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 12:17:37 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 字典元素的高级添加
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from collections import defaultdict


# 一个键映射多个值，那么你就需要将这多个值放到另外的容器中
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

print(d['a'])


# 保持元素的插入顺序, 使用列表
d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(2)
print(d)

# 去掉重复元素, 使用集合, 不关注元素顺序
d = defaultdict(set)
d['a'].add(1)
d['a'].add(1)
d['b'].add(4)
print(d)


# 将数据添加到多值映射的字典
pairs = {
    ('a', 12),
    ('a', 13),
    ('b', 14)
}
# 不用先创建 d['a'] = []
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)
