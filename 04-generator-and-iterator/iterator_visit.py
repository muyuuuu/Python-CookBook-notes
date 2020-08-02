'''
File: iterator_visit.py
Project: 04-generator-and-iterator
===========
File Created: Thursday, 23rd July 2020 3:55:22 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Thursday, 23rd July 2020 3:55:26 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 迭代器的访问
Copyright <<projectCreationYear>> - 2020 Your Company, <<XDU>>
'''
from itertools import dropwhile, islice, permutations, combinations, combinations_with_replacement, \
    zip_longest, chain, islice
from collections.abc import Iterable


# 迭代器切片
def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# 在迭代器和生成器上做切片操作，起始值与结束值
# 不能切片索引，因为它们的长度事先我们并不知道(并且也没有实现索引)。 
# 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。 
# 然后才开始一个个的返回元素，并直到切片结束索引位置。
# 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 
# 必须考虑到迭代器是不可逆的这个事实。 
# 所以如果你需要之后再次访问这个迭代器的话，那你就得先将它里面的数据放入一个列表中。
for x in islice(c, 10, 20):
    print(x)


# 跳过可迭代对象的开始部分
with open('/etc/passwd') as f:
    # 去掉文件头部的行
    for line in dropwhile(lambda line: not line.startswith('#'), f):
    # 如下的写法会去掉注释行
    # lines = (line for line in f if not line.startswith('#'))
        print(line, end='')


# 跳过指定位置的元素
items = ['a', 'b', 'c', 1, 4, 10, 15]
# [3:] 和 [:3]
for x in islice(items, 3, None):
    print(x)
for x in islice(items, None, 3):
    print(x)


# 排列组合的迭代, 你想迭代遍历一个集合中元素的所有可能的排列或组合
items = ['a', 'b', 'c']

# 全部的排列组合
for p in permutations(items):
    print(p)
# 指定数量的排列组合
for p in permutations(items, 2):
    print(p)
# 去除元素相同的排列组合（不考虑顺序）
for i in combinations(items, 2):
    print(i)
# 元素被选取就会从候选中剔除掉, 就不会再考虑它
for c in combinations_with_replacement(items, 3):
    print(c)
# 负责的迭代可以参考 itertools


# 迭代时添加索引
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
for n, (x, y) in enumerate(data, 1):
    print(n, x, y, sep=':')


# 同时迭代多个序列
a = [1, 2, 3]
b = [10]
c = ['w', 'x', 'y', 'z']
# 相比于 zip 而言，能处理不等长的序里
for i in zip_longest(a, b, c, fillvalue=0):
    print(i)


# 等长序列可转换为字典
d = [1, 2, 3, 4]
s = dict(zip(c, d))
print(s)


# 不同类型的数据一起迭代
s = {1, 2, 3}
# 不同集合元素的访问
for x in chain(c, s):
    print(x)
    # 或者对两个集合中的元素进行操作


# 将一个嵌套的序列展开为单个列表
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            # 类似于：for i in flattern(x): yield i
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

