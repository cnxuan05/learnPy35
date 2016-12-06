# coding:utf-8
# author:cnxuan05
PIE = 100


def func01():
    name = 'cnxuan 05'
    name2 = name
    name = "pao che ge"
    # 姓名  = '可见的中文字符' 变量名只能是英文单词
    gf_of_oldboy = "chen rong hua"
    global PIE
    PIE = 1000  # 常量不应该改变
    print('my name is:', name, '=', PIE)


def func02():
    age_of_olfboy = 40
    guess_age = int(input("guess age:\n"))
    print(str(guess_age))

