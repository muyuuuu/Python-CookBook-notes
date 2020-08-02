'''
File: custom_class.py
Project: 08-class
File Created: Saturday, 25th July 2020 9:42:52 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 9:42:54 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 定制类


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()
