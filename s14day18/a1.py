# coding:utf-8
from lxml import etree
import requests
import time
file_name = 'text_new_'


for kk in range(1, 1000):
    ss_list = []
    url = 'http://guyeshanren2011.com/weibo/%E5%A7%91%E5%B0%84%E5%B1%B1%E4%BA%BA2011?page=' + str(kk)
    url2 = 'http://guyeshanren2011.com/weibo/%E5%A7%91%E5%B0%84%E5%B1%B1%E4%BA%BA2011theone?page=' + str(kk)

    # http://guyeshanren2011.com/latestweibo?page=2
    print(url2)

    # /html/body/div/a[1]/h4
    html = requests.get(url2).text    #这里一般先打印一下html内容，看看是否有内容再继续。
    #time.sleep(1)
    s = etree.HTML(html)
    #title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div/a')
    for i in range(1,100):
        sstring = '/html/body/div/a[%s]/h4/text()' % str(i)
        stime = s.xpath(sstring)
        if not stime:
            continue

        sstring = '/html/body/div/div[%s]/p/text()' % str(i)
        sbody = s.xpath(sstring)
        if sbody:
            pass
            #print(sbody[0])

        need_data = '%s###%s' % (stime, sbody)
        #print(need_data)
        ss_list.append(need_data)
        new_file_name = file_name + str(kk).zfill(3)
        with open(new_file_name, 'w') as fp:
            for line in ss_list:
                fp.write(line + '\n')

# /html/body/div/div[2] /html/body/div/div[1]/p v/html/body/div/div[1]/p /html/body/div/div[2]/p/text()
# /html/body/div/a[2]/h4 /html/body/div/a[1]/h4 v/html/body/div/div[1]/p/text() /html/body/div/div[8]/p
























