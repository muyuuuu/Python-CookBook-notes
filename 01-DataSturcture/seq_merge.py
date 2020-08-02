'''
File: seq_merge.py
Project: 01-DataSturcture
===========
File Created: Thursday, 23rd July 2020 5:35:38 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Thursday, 23rd July 2020 5:35:50 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 两个序列排序
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
import heapq


a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# 所有输入序列必须是排过序的
for c in heapq.merge(a, b):
    print(c)
