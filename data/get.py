#coding:utf-8

file_name = 'novel.txt'

with open(file_name, 'r') as fp:
    sss = []
    a1 = '2012-10-30 03:41:00'
    a2 = '2020年7月21日'

    import re

    temp = []
    #if 1==1:
    #    la = a1
    for la in fp.readlines():


        #print(la)

        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", la)
        mat2 = re.search(r"(\d{4}年\d{1,2}月\d{1,2})", la)


        if mat or mat2:
            #print('find')
            sss.append(temp)

            temp = []
            temp.append(la)
        else:
            temp.append(la)

        #break
    #print(sss)
    for u in sss:
        print(' '.join(u))




print('123')