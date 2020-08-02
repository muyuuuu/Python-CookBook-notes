'''
File: seq_slice.py
Project: DataSturcture
===========
File Created: Monday, 20th July 2020 10:48:44 am
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 11:42:46 am
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 序列元素分解
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

# 全部分解
data = (12, 34)
x, y = data
print(x, y)


# 忽略不想要的元素
data = [1, 2, 3, 4, [5, 6]]
_, a, _, _, b = data
print(a, b)


# 一个变量接收多个变量
# 计算学生的平均成绩
score = [1, 78, 87, 98, 100]
def avg_score(score):
    first, *middle, last = score
    print(sum(middle) / len(middle))
avg_score(score)


# 忽略多个变量
*_, last = score
print(last)


# 处理变长参数
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    print(tag, '--->', *args)
