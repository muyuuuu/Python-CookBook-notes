'''
File: enumerate.py
Project: 08-class
File Created: Saturday, 25th July 2020 10:48:54 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 10:48:56 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 枚举类
from enum import Enum


class Letter(Enum):
   A = 1
   B = 2
   C = 3

print({i.name: i.value for i in Letter})
print(Letter.A.value)
