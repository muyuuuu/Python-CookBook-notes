'''
File: father_class.py
Project: 08-class
File Created: Sunday, 26th July 2020 5:29:20 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Sunday, 26th July 2020 5:29:22 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 调用父类方法（还没领悟精髓）
'''
class A:
    def __init__(self):
        self.x = 0
    def spam(self):
        print('A.spam was called')


class B(A):
    def __init__(self):
        # super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了：
        super().__init__()
        self.y = 1
    def spam(self):
        print("B.spam was called")
        # 调用父类的方法
        super().spam()


b = B()
print(b.x)
b.spam()

# 调用父类方法
