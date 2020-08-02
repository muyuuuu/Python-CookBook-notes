'''
File: multi-ingeritance.py
Project: 08-class
File Created: Saturday, 25th July 2020 9:36:51 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 9:36:53 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 多重继承


class Animal(object):
    pass


class Flyable(object):
    def fly(self):
        print('Flying...')


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# 在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
class Bat(Animal, Flyable):
    pass


b = Bat()
b.fly()
