#coding:utf-8


import random
def a():

    return random.randint(2,3)

def b():
    sum = 0
    for i in range(3):
        dd = a()
        #print(dd)
        sum += dd
        pass
    return sum

def c():
    sa = 0
    s1 = []
    s2 = []

    def is_odd(n):
        data = 0
        if n % 2 == 0:
            print(0)
        else:
            print(1)
        #return n % 2 == 1
    #
    # newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print(newlist)


    for i in range(6):
        sss = b()
        sa += sss

        s1.append(sss)


        if sss == 9:
            s2.append(6)
        elif sss == 8:
            s2.append(9)
        else:
            s2.append(sss)

    print('s1', s1)
    print('s2', s2)

    newlist = filter(is_odd, s1)
    for u in newlist:
       print(u)
    print('###')
    newlist = filter(is_odd, s2)
    for u in newlist:
       print(u)
    print(55 - sum(s1))
    print(55 - sum(s2))
    return
d = c()
print(d)
