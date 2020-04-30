# coding:utf-8


import random
import time


def generate_taichi():
    return random.randint(2, 3)


def generate_piece():
    # pics = list()
    sums = 0
    sums += generate_taichi()
    sums += generate_taichi()
    sums += generate_taichi()
    return sums


def generate_gua():
    pre_gua = list()
    aft_gua = list()
    for i in range(6):
        n_data = generate_piece()
        pre_gua.append(n_data)
        if 9 == n_data:
            aft_gua.append(6)
        elif 8 == n_data:
            aft_gua.append(9)
        else:
            aft_gua.append(n_data)
    # print(list(pre_gua))
    # print(list(aft_gua))
    print('#' * 6)

    new_pre_gua = [0 if m % 2 == 0 else 1 for m in pre_gua]
    get_sixth_eight(new_pre_gua)

    print(get_rank_num(55 - sum(pre_gua)))
    print('#' * 6)

    new_aft_gua = [0 if m % 2 == 0 else 1 for m in aft_gua]
    get_sixth_eight(new_aft_gua)

    print(get_rank_num(55 - sum(aft_gua)))
    print('#' * 6)
    return


def get_eight(p_list):
    if p_list == [1, 1, 1]:
        return '天'
    if p_list == [0, 0, 0]:
        return '地'
    if p_list == [1, 0, 1]:
        return '火'
    if p_list == [0, 1, 0]:
        return '水'
    if p_list == [0, 1, 1]:
        return '风'
    if p_list == [1, 1, 0]:
        return '泽'
    if p_list == [1, 0, 0]:
        return '雷'
    if p_list == [0, 0, 1]:
        return '山'


def get_sixth_eight(q_list):
    sum_info = [
        '天天乾', '天风姤', '天山遁', '天地否', '风地观', '山地剥', '火地晋', '火天大有',
        '水水坎', '水泽节', '水雷屯', '水火既济', '泽火革', '雷火丰', '地火明夷', '地水师',
        '山山艮', '山火贲', '山天大畜', '山泽损', '火泽睽', '天泽履', '风泽中孚', '风山渐',
        '雷雷震', '雷地豫', '雷水解', '雷风恒', '地风升', '水风井', '泽风大过', '泽雷随',
        '风风巽', '风天小畜', '风火家人', '风雷益', '天雷无妄', '火雷噬嗑', '山雷颐', '山风蛊',
        '火火离', '火山旅', '火风鼎', '火水未济', '山水蒙', '风水涣', '天水讼', '天火同人',
        '地地坤', '地雷复', '地泽临', '地天泰', '雷天大壮', '泽天夬', '水天需', '水地比',
        '泽泽兑', '泽水困', '泽地萃', '泽山咸', '水山蹇', '地山谦', '雷山小过', '雷泽归妹',

    ]
    lower = q_list[0:3]
    upper = q_list[3:]
    # print(lower)

    print(get_eight(upper))
    print(get_eight(lower))
    for elem in sum_info:
        if elem[0] == get_eight(upper) and elem[1] == get_eight(lower):
            print(elem[2:])

    return


def get_rank_num(pnum):
    if pnum <= 6:
        return pnum
    elif pnum <= 11 and pnum > 6:
        return 12 - pnum
    elif pnum <= 16 and pnum > 11:
        return pnum - 10
    elif pnum <= 21 and pnum > 16:
        return 22 - pnum

    return


def fre_create():
    import time
    from tqdm import tqdm

    for u in range(9999):
        generate_gua()
        # time.sleep(60)

        mylist = range(60)
        for i in tqdm(mylist):
            time.sleep(1)

    return


if __name__ == '__main__':
    fre_create()

    pass
