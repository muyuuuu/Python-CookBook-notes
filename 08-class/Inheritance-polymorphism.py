'''
File: Inheritance-polymorphism.py
Project: 08-class
File Created: Saturday, 25th July 2020 8:39:40 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 8:39:44 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 继承和多态


class Animal(object):
    def __init__(self, age):
        self.__age = age

    def run(self):
        print('Animal is running...')

    def get_age(self):
        print(self.__age)

# 继承，子类获得了父类的全部功能
class dog(Animal):
    def eat(self):
        print("dog is eating...")

a = dog(12)
a.run()
a.eat()
a.get_age()


# 多态
class Cat(Animal):
    # 子类的run()覆盖了父类的run()
    def run(self):
        print('Cat is running...')


b = Cat(14)
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，
# 不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run()等函数。
b.run()
b.get_age()
