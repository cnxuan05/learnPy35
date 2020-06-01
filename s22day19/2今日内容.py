# coding:utf-8
import re

text = "s127 3628391387 17648372936 183930627 17648372930 28649703767"
m = re.findall(r"1[3-9]\d{9}", text)
print(m)
