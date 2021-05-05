#coding:utf-8

#将你的xpath复制到三引号里面，因为xpath里可能有双引号，所以我们加上三引号比较靠谱

"""
http://guyeshanren2011.com/weibo/%E5%B1%B1%E4%BA%BA2011theone?page=2
/html/body/div/div[1]/p/text()[2]
/html/body/div/div[4]/p/text()[3]
v
/html/body/div/a[2]/h4
"""

def a():
    s=selecter.xpath("""/html/body/div/div[1]/p/text()""")
    title=selecter.xpath("""/html/body/div/a[2]/h4/text()""")
    print(title)
    #mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", str(title))
    mat = re.search(r"(\d{4}年\d{1,2}月\d{1,2}日\s\d{1,2}:\d{1,2}:\d{1,2})", str(title))

    print (mat.group())

def read_page():
    import requests

    import re
    from lxml import etree
    import lxml


    for page_num in range(1,100):
        url = "http://guyeshanren2011.com/weibo/%E5%B1%B1%E4%BA%BA2011theone?page=" + str(page_num)
        # 你需要爬取的网页
        html = requests.get(url)
        html.encoding = "utf-8"
        selecter = etree.HTML(html.text)

        for i in range(1,30):
            #selecter = etree.HTML(html.text)
            #print(selecter)
            rule2 = "/html/body/div/div[" + str(i) +"]/p/text()"
            rule3 = "/html/body/div/a[" + str(i) + "]/h4/text()"

            #print(rule2,rule3)
            title = selecter.xpath(rule3)
            #print(title)
            mat = re.search(r"(\d{4}年\d{1,2}月\d{1,2}日\s\d{1,2}:\d{1,2}:\d{1,2})", str(title))
            if mat:
                print(mat.group())
                sstring = selecter.xpath(rule2)
                print(sstring)




read_page()

print('over')
