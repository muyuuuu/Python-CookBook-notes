'''
File: slot.py
Project: 08-class
File Created: Saturday, 25th July 2020 9:11:13 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 9:11:15 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 使用__slots__
# 限制实例的属性，不允许创建规定以外的属性
# 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。


class People(object):

    __slots__ = ('__name', '__age') 

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        print(self.__name, self.__age, sep=', ')


p = People('ljw', 22)
p.get_info()


# 对继承的子类是不起作用的
class Student(People):
    pass


s = Student('bart', 14)
s.pos = "beijing"
print(s.pos)


# 多继承
class Pos(object):
    __slots__ = '__pos'
    def __init__(self, pos):
        self.__pos = pos


class worker(People, Pos):
    pass
    # def __init__(self, name, age, pos):
    #     People.__init__(self, name, age)
    #     Pos.__init__(self, pos)


# s = worker('ljw', 12, 'Shanghai')
# s.gender = 1
# print(s.gender)

# 另外，定义了slots后的类不再支持一些普通类特性了，比如多继承。 
# 大多数情况下，你应该只在那些经常被使用到的用作数据结构的类上定义slots (比如在程序中需要创建某个类的几百万个实例对象)。
