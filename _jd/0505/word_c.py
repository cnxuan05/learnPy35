#coding:utf-8


import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

# 958条评论数据
with open('2013.txt',encoding='utf-8') as f:
    data = f.read()

# 文本预处理  去除一些无用的字符   只提取出中文出来
new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
new_data = " ".join(new_data)

# 文本分词
seg_list_exact = jieba.cut(new_data, cut_all=True)

result_list = []
with open('stop_words.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
        i = i.replace("\n", "")   # 去掉读取每一行数据的\n
        stop_words.add(i)

for word in seg_list_exact:
    # 设置停用词并去除单个词
    if word not in stop_words and len(word) > 1:
        result_list.append(word)
print(result_list)

stop_words = ["我","你","她","的","是","了","在","也","和","就","都","这"]

import numpy as np
img = Image.open("640.png") # 打开遮罩图片
mask = np.array(img) #将图片转换为数组



# 筛选后统计
word_counts = collections.Counter(result_list)
# 获取前100最高频的词
word_counts_top100 = word_counts.most_common(100)
print(word_counts_top100)

# 绘制词云
my_cloud = WordCloud(
    mask=mask,
    background_color='white',  # 设置背景颜色  默认是black
    width=900, height=600,
    max_words=1000,            # 词云显示的最大词语数量
    font_path='SimHei.ttf',   # 设置字体  显示中文
    max_font_size=99,         # 设置字体最大值
    min_font_size=16,         # 设置子图最小值
    random_state=50           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(word_counts)

# 显示生成的词云图片
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.show()

my_cloud.to_file('2013.jpg')











