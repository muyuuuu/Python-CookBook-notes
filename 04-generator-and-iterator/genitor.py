'''
File: genitor.py
Project: 04-generator-and-iterator
===========
File Created: Thursday, 23rd July 2020 3:02:26 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Thursday, 23rd July 2020 3:02:30 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 生成器
Copyright <<projectCreationYear>> - 2020 Your Company, <<XDU>>
'''
from collections import deque


# 生成器暴露外部状态给用户
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        # 索引从 1 开始
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


# 创建一个实例对象，可以访问内部属性值
# 如果你在迭代操作时不使用for循环语句，那么你得先调用 iter() 函数
with open('demo.py') as f:
    lines = linehistory(f)
    for line in lines:
        for lineno, hline in lines.history:
            print('{}:{}'.format(lineno, hline), end='')


f = open('demo.py')
lines = linehistory(f)
t = iter(lines)
print(next(t))
