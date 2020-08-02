'''
File: object_info.py
Project: 08-class
File Created: Saturday, 25th July 2020 8:52:05 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 8:52:07 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 获取对象信息


class link:
    def __init__(self):
        self.x = 1
        self.__q = []

    def add(self, a):
        self.__q.append(a)

    # 实现  len(obj) 
    def __len__(self):
        return 100 - len(self.__q)

    def get_link(self):
        return self.__q


a = link()
a.add(1)
a.add(2)

print(a.get_link())
print(len(a))

# 获取属性
# 没有
b = getattr(a, '__q', 404)
print(type(b))

# 有
b = getattr(a, 'x', 404)
# 获取属性并赋值
print(b)
# 获取方法并执行
b = getattr(a, 'get_link', 404)
c = b()
print(c)
print(hasattr(a, 'x'))
