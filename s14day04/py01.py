# coding:utf-8
# __author__:cnxuan05

import time


# 本质是函数
# 不能修改被装饰的函数的调用方式

# 函数即变量
# 高阶函数 = 把一个函数名当实参传递
# 返回值中包含函数名


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('time is %s\n' % (stop_time - start_time))

    return wrapper


@timer
def hello():
    time.sleep(1.3)
    print('123')


# hello()


def foo():
    print('in the foo')
    bar()
    pass


def bar():
    print('in the bar')
    pass


# foo()


# 迭代器 生成器

# 循环调用
a = [i * 2 for i in range(10)]

# print(a)
b = (i * 2 for i in range(100000000))


# 生成器只有在调用时才会生成相应的数据

# 生成器只记住当前的位置 只有一个__next__()方法

# 第二种生成器

def fib(max_num):
    count, m1, m2 = 0, 0, 1
    while count < max_num:
        yield m2
        m1, m2 = m2, m1 + m2
        count = count + 1

    return 'done'


# yield方法实现并行计算的效果
def consumer(name):
    print(name)
    while True:
        baozi = yield
        print('get %s 123 %s' % (baozi, name))
    pass


# 单线程下的并行效果
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()

    print('开始做包子')
    for i in range(10):
        time.sleep(1)
        print('baozi 分2半')
        c.send(i)
        c2.send(i)
        pass
    pass


# d = consumer('阿拉')
# d.__next__()
#
# b1 = '韭菜馅'
# d.send(b1)      # 唤醒再传值
#
# d.__next__()    # 单纯调用不会传值
#
# d.__next__()    # 只唤醒
#
# d.__next__()
# producer('lilei')


from collections import Iterable

print(isinstance('abc', Iterable))

# 可以被next()函数调用并不断返回下一个值的对象
# 惰性的 表示一个无限大的数据流

a = [102, 123, 1, 2, 12, 123]
b = iter(a)
print(b)
#


# 内置函数
# print(all([0, -1, 12, 3, 123]))
# print(any([1, -1, 0, 3, 123]))

res = filter(lambda n: n > 5, range(10))
res2 = map(lambda n: n ** 2, range(10))
res3 = [lambda i: i * 2 for i in range(10)]

# 内置方法

import functools

res4 = functools.reduce(lambda x, y: x + y, range(3, 10))
# print(res4)

# print(globals().get('local_var'))
# print(locals())

# 一切皆对象
# 有对象就有属性
a = {6: 2, 8: 0, -5: 5, 9: 11}

# 按key 进行排序
# print(sorted(a.items()))

# 按val 进行排序
print(sorted(a.items(), key=lambda x: x[1]))


# 序列化 -- 内存的数据对象存到硬盘上
# 反序列化 -- 硬盘的数据加载到内存


import pickle
# 默认变成二进制
# 函数名一样即可
# 序列化的是整个的数据对象

# 文件夹 路径



















#
