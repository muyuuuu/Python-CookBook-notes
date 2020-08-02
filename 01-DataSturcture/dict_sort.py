'''
File: dict_sort.py
Project: DataSturcture
===========
File Created: Monday, 20th July 2020 5:24:37 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 5:24:58 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 字典排序
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from collections import OrderedDict
from operator import itemgetter


# 保留元素插入时的顺序
# 大小是一个普通字典的两倍，因为它内部维护着另外一个插入顺序排序的链表。
d = OrderedDict()
d['foo'] = 1
d['spam'] = 3
d['bar'] = 2
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])


# 按照某一规定排序
data = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# 传入排序的参数
rows_by_fname = sorted(data, key=itemgetter('fname'))
rows_by_uid = sorted(data, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# 传入多个参数，先比较第一个，相同则比较第二个
rows_by_lfname = sorted(data, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# 输出最大值和最小值
b = min(data, key=itemgetter('uid'))
a = max(data, key=itemgetter('uid'))

print(a, '\n', b)
