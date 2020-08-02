'''
File: demo.py
Project: 04-generator-and-iterator
===========
File Created: Thursday, 23rd July 2020 10:36:53 am
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Thursday, 23rd July 2020 10:37:00 am
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 迭代器
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
import itertools


# __iter__ 方法支持迭代
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    # 将迭代请求传递给内部的 _children 属性。
    # 调用 _childrem.__iter__() 方法来返回对应的迭代器对象
    # 如果一个容器类提供了 __iter__() 方法，并且该方法能返回一个能够逐个访问容器内所有元素的迭代器，
    # 则我们说该容器类实现了迭代器协议。
    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
# Outputs Node(1), Node(2)
for ch in root:
    print(ch)


# 生成器
# 普通函数不同的是，生成器只能用于迭代操作
def countdown(n):
    while n > 0:
        yield n
        n -= 1
    print('Done')

a = countdown(6)
# 一旦生成器函数返回退出，迭代终止
for i in a:
    print(i)


# 反向迭代
# 对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# 反向迭代
for rr in reversed(Countdown(3)):
    print(rr)

# 正向迭代
for rr in Countdown(3):
    print(rr)
