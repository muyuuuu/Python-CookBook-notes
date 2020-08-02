'''
File: priority_queue.py
Project: DataSturcture
===========
File Created: Monday, 20th July 2020 12:01:48 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 12:03:08 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 实现优先级队列 
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

import heapq


# 优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 队列中插入元素，并不按照优先级排序
        # 加入索引，防止俩个优先级相同的没法比较
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 返回最小的元素，-1 表示取出 item
        return heapq.heappop(self._queue)[-1]


# 插入项
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
a = Item('aoo')
b = Item('boo')
c = Item('coo')

q.push(a, 1)
q.push(b, 2)
q.push(c, 1)

# a 的索引小于 c，所以先弹出 a
print(q.pop())
print(q.pop())
print(q.pop())
