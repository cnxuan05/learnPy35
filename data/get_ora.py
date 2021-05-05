import cx_Oracle  # 引用模块cx_Oracle

conn = cx_Oracle.connect('system/oracle@192.168.1.61/xe')  # 连接数据库
c = conn.cursor()  # 获取cursor
x = c.execute('select * from shop.ACCOUNTS_BLOGUSER')  # 使用cursor进行各种操作
data = x.fetchone()
print(data, type(data))
c.close()  # 关闭cursor
conn.close()  # 关闭连接
