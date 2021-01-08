'''
File: anonymous.py
Project: 07-function
File Created: Saturday, 25th July 2020 5:04:24 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 5:06:03 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
import math

# 匿名函数
# 冒号前是参数，冒号后是返回的结果
add = lambda x, y: x + y
print(add(1, 2))
print(add('str', 'ing'))

names = ['David Beazley', 'Brian Jones',
        'Raymond Hettinger', 'Ned Batchelder']
names.sort(key=lambda name: name.split()[-1].lower())
print(names)


# 匿名函数中的变量值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# 变量在运行时绑定，而不是定义时绑定
print(a(10))
print(b(10))

# 也可以定义时绑定
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

# 多个数值的比较并排序
center = (4.2, 6.7)
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

points.sort(key=lambda p: distance(center, p))
print(points)