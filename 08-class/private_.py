'''
File: private_.py
Project: 08-class
File Created: Saturday, 25th July 2020 8:29:38 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 8:29:40 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问。
# 不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。


class Student(object):

    def __init__(self, name, score, age):
        self.__name = name
        self.__score = score
        self._age = age

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('bart', 98, 14)
# 错误
# 确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# print(bart.__name)
bart.print_score()

# 当然也可以获取私有变量
a = bart.get_name()
print(a)

# 通过外部代码修改 score
bart.set_score(97)
bart.print_score()

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量，
# 所以，不能用__name__、__score__这样的变量名。

# _name 单下划线可以访问，但视为私有变量，不要轻易访问
print(bart._age)


# 大多数而言，你应该让你的非公共名称以单下划线开头。
# 但是，如果你清楚你的代码会涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案。
# 双下划线可以通过 _B__private 方式进行访问，防止子类继承导致的覆盖


class B:
    def __init__(self):
        self.__private = 0
        # 会被继承
        self._private = 12


class C(B):
    def __init__(self):
        super().__init__()
        # 不继承 B 中的私有变量
        self.__private = 1 

a = C()
print(a._private)
