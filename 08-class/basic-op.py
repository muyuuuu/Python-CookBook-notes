'''
File: basic-op.py
Project: 08-class
File Created: Saturday, 25th July 2020 8:19:22 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 8:20:04 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 类和实例


class Student(object):
    # 类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 直接操作了对象内部的数据，但无需知道方法内部的实现细节。
    # 这些数据和逻辑被“封装”起来了
    def print_info(self):
        print('%s: %s' % (self.name, self.score))

# 传入参数不能为空
bart = Student('Bart Simpson', 59)
print(bart.name, bart.score, sep=', ')

# 数据封装
bart.print_info()

# 绑定额外属性
bart.age = 8
print(bart.age)
