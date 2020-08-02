'''
File: property.py
Project: 08-class
File Created: Saturday, 25th July 2020 9:16:43 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 9:16:46 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# Python内置的@property装饰器就是负责把一个方法变成属性调用
# 防止代码的冗余
import math


class Student(object):

    def __init__(self, score):
        self._score = score

    # Getter function 方法转属性
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # del s.score 出发
    @score.deleter
    def score(self):
        raise AttributeError("Can't delete attribute")


s = Student(89)
# 方法转属性
print(s.score)

# 直接改属性，不推荐
s._score = 90
s.set_score = 98
# 方法变成属性赋值，于是就拥有一个可控的属性操作
print(s.score)


# 不要写这种没有做任何其他额外操作的property。 
# 首先，它会让你的代码变得很臃肿
# 其次，它还会让你的程序运行起来变慢很多
class People(object):

    @property
    def birth(self):
        return self._birth

    # 没有初始化时，不能改动函数名
    @birth.setter
    def birth(self, value):
        self._birth = value

    # 设置为只读属性
    @property
    def age(self):
        return 2020 - self._birth


s = People()
s.birth = 1998
# 赋值会错误
# s.age = 23
print(s.age)


# 动态计算attribute的方法。 这种类型的attributes并不会被实际的存储，而是在需要的时候计算出来。
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.perimeter)


# 不要像下面这样写有大量重复代码的property定义(具体如何修改需要参考后文)
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value


# 子类中扩展property
