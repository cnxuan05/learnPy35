# coding:utf-8
# author:cnxuan05

def func01():
    names = ['alex', 'tenglan', 'eric', 'oldboy']
    s = set([3, 5, 7, 9])  # 通过下标访问元素 下标从0 开始计数
    t = set("hello")
    a = t | s  # 求并集

    print(a)
    pass


def func02():
    list_1 = [1, 2, 67, 23, 4, 123, 4, 123, 5, 23, 80, 2, 4, 9, 3]

    list_2 = set([1, 2, 2342, 123123, 24234, 75467, 345345])

    print(set(list_1).union(list_2))  # 求并集
    # print(set(list_1)&list_2)
    print(set(list_1).intersection(list_2))  # 求交集

    print(set(list_1).difference(list_2))  # 求差集
    pass


def func03():
    list_1 = set("hello")
    list_2 = set("he")
    # 求子集
    print(list_2.issubset(list_1))
    print(list_1.issuperset(list_2))

    # 求对称差集
    print(list_1.symmetric_difference(list_2))

    a = list_1 | list_2
    b = list_1 & list_2
    c = list_1 - list_2
    d = list_1 ^ list_2
    print(a, b, c, d)
    a.add('x')
    a.remove('x')
    a.update(set('news'))

    print(a)
    print(len(a))
    print('x' in a)
    print('y' not in a)
    print(b.issubset(a))
    print(a.issuperset(b))
    print(a.pop())
    # (a.remove('long'))
    print(a.discard('long'))
    pass


def func04():
    import sys
    # sys.path.append('lyrics.txt')
    f = open("lyrics.txt", 'r', encoding='utf-8')

    first_line = f.readline()
    # print('get', first_line)
    data = f.read()
    # print(type(data), data)
    count = 0
    f = open("lyrics.txt", 'r', encoding='utf-8')
    f.read(5)
    print('##')
    print(f.tell())

    f.seek(0)
    # for line in f:
    #     print(line)
    #     count += 1
    # print(count)
    # print('####'  *10)
    # for index,line in enumerate(f.readlines()):
    #     if index == 3:
    #         continue
    #     print(index,line)
    # for u in f.readlines():
    #     print(u.strip())
    # for u in range(5):
    #     print(f.readline())
    # f.write(data)
    # f.write('我爱北京天安门')
    f.close()
    pass


def func05(x, *args):
    print((args))  # 函数的非固定参数 处理为元组的形式

    # 默认参数
    # 参数组 == 默认参数(在函数调用时可有可无) 关键字参数(形参存在) 位置参数
    # 实参的数目不固定


    pass


def func06(**kwargs):
    print(kwargs)
    pass


# func05(*(1, 2, 3, 4, 5))
# func06(name='alex', age='9')










