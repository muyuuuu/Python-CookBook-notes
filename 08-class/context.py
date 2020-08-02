'''
File: context.py
Project: 08-class
File Created: Sunday, 26th July 2020 11:49:26 am
Author: lanling (https://github.com/muyuuuu)
-----------
Last Modified: Sunday, 26th July 2020 11:49:28 am
Modified By: lanling (https://github.com/muyuuuu)
Copyright 2020 - 2020 NCST, NCST
-----------
@ 佛祖保佑，永无BUG--
'''
# 让对象支持上下文管理协议 with只能配合上下文管理器使用
from functools import partial
from socket import socket, AF_INET, SOCK_STREAM


# 为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        # 它返回的值(如果有的话)会被赋值给 as 声明的变量
        # 否则类型为空
        return self.sock

    # 三个参数是异常类型、异常值和追溯信息(如果有的话)。
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
        

# 初始化的时候并不会做任何事情
conn = LazyConnection(('www.python.org', 80))

# 连接的建立和关闭是使用 with 语句自动完成的
with conn as s:
    # 先执行上下文管理器的__enter__方法，然后再执行语句体，执行完语句体后，最后执行__exit__方法
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed


# 异常捕捉测试
class Foo(object):

    def __init__(self):
        print('initialization')

    def __enter__(self):
        print('enter')

    # 出现异常时，如果 __exit__ 返回 False（默认不写返回值时，即为False），
    # 则会重新抛出异常，让with 之外的语句逻辑来处理异常，这也是通用做法；
    # 如果返回 True，则忽略异常，不再对异常进行处理
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        # return True

obj = Foo()

# 正常情况，执行到报错地方就不会执行了，而__exit__是在语句体执行完之后执行的
# 但还是执行了__exit__方法；当我们在__exit__中给一个返回值为Ture时，就会忽略错误。
with obj:
    raise ImportError
    # 不会被执行
    print('run')


# 嵌套连接 允许多个 with 语句来嵌套使用连接
class LazyConnection1:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    # __enter__() 方法执行的时候，它复制创建一个新的连接并将其加入到栈里面。 
    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    # __exit__() 方法简单的从栈中弹出最后一个连接并关闭它。
    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


conn = LazyConnection1(('www.python.org', 80))
# 实现多层嵌套连接
with conn as s1:
    pass
    with conn as s2:
        pass
        # s1 and s2 are independent sockets

# 在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。 
# 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。 
# 例如，如果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生死锁。 
# 通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免这些问题
# 因为 __exit__() 方法可以让你无需担心这些了。
