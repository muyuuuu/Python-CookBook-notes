'''
File: obj-instance.py
Project: 08-class
File Created: Saturday, 25th July 2020 9:01:57 pm
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Saturday, 25th July 2020 9:01:59 pm
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 实例属性和类属性


# 类本身需要绑定一个属性，属性是类属性
# 实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
class Student(object):
    name = 'Student'


# 创建实例s
s = Student() 

# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name) 

# 打印类的name属性
print(Student.name) 

# 给实例绑定name属性
s.name = 'Michael' 
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name) 

# 但是类属性并未消失，用Student.name仍然可以访问
print(Student.name) 

# 如果删除实例的name属性
del s.name 
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name) 
