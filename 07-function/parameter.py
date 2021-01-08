'''
File: parameter.py
Project: 07-function
File Created: Saturday, 25th July 2020 4:20:32 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 4:20:35 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
from functools import partial
import math


# 接受任意数量的位置参数
def avg(first, *rest):
    return first + sum(rest)

print(avg(1, 2))
print(avg(1, 2, 3, 4))


# 接受任意数量的关键字参数
# attrs是一个包含所有被传入进来的关键字参数的字典。
def foo(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    if 'a' in kwargs.keys():
        print(kwargs['a'])
    # print(kwargs['a'])
    print('---------------------------------------')

foo(1, 2, 3, 4)
foo(a = 1, b = 2, c = 3)
foo(1, 2, 3, 4, a = 1, b = 2, c = 3)
foo('a', 1, None, a = 1, b = '2', c = 3)


# 同时接受任意数量的位置参数和关键字参数
# *args 只能作为最后一个位置参数
def anyargs(*args, **kwargs):
    # 位置参数放到元祖中
    print(args) # A tuple
    # 关键字参数放到字典中
    print(kwargs) # A dict


# 希望函数的某些参数强制使用关键字参数传递
def recv(maxsize, *, block):
    return 2

# recv(1024, True) # TypeError
# 必须传递关键字的参数
recv(1024, block=True) # Ok


# 预先指定关键字参数
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))


# 减少可调用对象的参数个数
def spam(a, b, c, d):
    print(a, b, c, d)

# 按照参数顺序传递参数
s1 = partial(spam, 1)
print(s1(2, 3, 4))
s3 = partial(spam, 1, 2, d=42)
print(s3(6))


# 多个数值的比较并排序
center = (4.2, 6.7)
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

# 只传入第一个参数，points为第二个传入参数
points.sort(key=partial(distance, center))
print(points)
# 等价
points.sort(key=lambda p: distance(center, p))
