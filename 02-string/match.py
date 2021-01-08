'''
File: match.py
Project: 02-string
===========
File Created: Wednesday, 22nd July 2020 9:46:39 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Wednesday, 22nd July 2020 10:14:54 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 字符串匹配
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

# 判断文件的后缀名
file_name = "test.txt"
print(file_name.endswith('.txt'))

# 判断字符串的前缀
url = 'http://www.python.org'
print(url.startswith('http'))

# 查找字符串
# 只返回第一次出现的位置
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))

# 字符串替换
text.replace('yeah', 'yep')
print(text)
text = text.replace('yeah', 'yep')
print(text)

# 删除两端空白
s = ' hello world \n'

# 删除开始或者结尾的空白
s.strip()
# 只删除左侧空白
s.lstrip()
# 只删除右侧空白
s.rstrip()
print(s)

# 删除指定字符串
t = '-----hello====='
t.lstrip('-')
a = t.strip('-=')
print(a)
