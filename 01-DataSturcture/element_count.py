'''
File: element_count.py
Project: 01-DataSturcture
===========
File Created: Monday, 20th July 2020 10:41:10 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Monday, 20th July 2020 10:41:15 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>>)
===========
Description: 序列中出现次数最多的元素
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
from collections import Counter


# 出现频率最高的3个单词
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# 字典，将元素映射到出现次数中
print(word_counts['look'])


# 更新词汇表
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(word_counts['eyes'])


# Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 
# 在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
a = Counter(words)
b = Counter(morewords)

# 直接操作
c = a + b
d = a - b
print(c, '\n', d)
