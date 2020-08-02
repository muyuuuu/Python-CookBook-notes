'''
File: class_output.py
Project: 08-class
File Created: Sunday, 26th July 2020 11:39:51 am
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Sunday, 26th July 2020 11:39:53 am
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 要改变一个实例的字符串表示，让它们更具可读性。
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__() 方法返回一个实例的代码表示形式
    # 内置的 repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    #  __str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串。
    # 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。
    def __str__(self):
        # 0实际上指的就是 self 本身
        return '({0.x}, {0.y})'.format(self)


p = Pair(3, 4)
print(p)

a = str(p)
print(p)
