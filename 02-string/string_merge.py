'''
File: string_merge.py
Project: 02-string
===========
File Created: Wednesday, 22nd July 2020 10:41:50 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Wednesday, 22nd July 2020 10:41:54 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 字符串合并
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

# 想合并的字符串在可迭代的序列中
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# 因为加号连接会引起内存复制以及垃圾回收操作
s = ' '.join(parts)
print(s)


# 想合并的字符串包括了其他类型
data = ['ACME', 50, 91.1]
s = ', '.join((str(d) for d in data))
print(s)


# 打印时简单的连接
a, b, c = 1, 2, 3
print(a, b, c, sep=':')


# 字符串很小考虑前者
# f.write(chunk1 + chunk2)

# 字符串很大考虑后者
# f.write(chunk1)
# f.write(chunk2)
