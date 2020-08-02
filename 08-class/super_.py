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
@ 佛祖保佑，永无BUG--
'''
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        # super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了：
        super().__init__()
        self.y = 1

b = B()
print(b.x)


# super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中
class Base:
    def __init__(self):
        print('Base.__init__')

class A1(Base):
    def __init__(self):
        # 父类的初始化
        super().__init__()
        # Base.__init__(self)
        print('A.__init__')

class B1(Base):
    def __init__(self):
        super().__init__()
        # Base.__init__(self)
        print('B.__init__')

class C(A1, B1):
    def __init__(self):
        super().__init__() 
        # A.__init__(self)
        # B.__init__(self)
        print('C.__init__')
