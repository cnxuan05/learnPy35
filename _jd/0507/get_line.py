#coding:utf-8

file_name = 'ca.tsv'

x = []
y = []

with open(file_name, 'r') as fp:
    for line in fp.readlines():
        #print(line)
        data = line.rstrip('\n').split('\t')
        #print(data)
        x.append(data[1]+data[2])
        #x.append('1')

        y.append(data[0])
print(x)
print(y)
x = x[0:12]
y = y[0:12]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
font_manager.fontManager.addfont('./SimHei.ttf')

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# x = np.arange('2017-08-01','2017-08-10',dtype=np.datetime64)
# y = np.random.randint(10,100,size=9)
# y2 = np.random.randint(10,100,size=9)


get_x=np.array(x)


get_y=np.array(y)


#font_path='SimHei.ttf'
plt.plot(get_x,get_y,color='red',label='APP')
#plt.plot(x,y2,color='blue',label='PC')

plt.title(u'发帖统计')
plt.xlabel(u'月份')
plt.ylabel(u'数量')
plt.xticks(rotation=-15)
plt.yticks(rotation=-15)

plt.legend()

#plt.show()

#plt.savefig('./test2.png')

import pandas as pd
import matplotlib.pyplot as plt

# 准备数据
data = {'sport_type':get_x,
        'score':get_y}
df = pd.DataFrame(data)

print(df)

# 绘制图形
plt.bar(df['sport_type'], df['score'])

#plt.show()

fig = plt.figure(figsize = (100,200))

import pandas as pd

import matplotlib.pyplot as plt
# 设置绘图风格
plt. style.use("ggplot")
# 设置中文编码和符号的正常显示
plt.rcParams["font.sans-serif"] = "KaiTi"
plt.rcParams["axes.unicode_minus"] = False

# 绘图
plt.plot(df.sport_type, # x轴数据
         df.score, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='brown') # 点的填充色
# 添加标题和坐标轴标签
plt.title('公众号每天阅读人数趋势图')
plt.xlabel('日期')
plt.ylabel('人数')

# 剔除图框上边界和右边界的刻度
plt.tick_params(top = 'off', right = 'off')

# 为了避免x轴日期刻度标签的重叠，设置x轴刻度自动展现，并且45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图形
plt.show()



print('over')

