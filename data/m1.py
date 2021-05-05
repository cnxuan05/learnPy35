# coding=utf-8
import MySQLdb

# connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
# 这只是连接到了数据库，要想操作数据库需要创建游标。
conn = MySQLdb.connect(
    host='192.168.1.61',
    port=3306,
    user='root',
    passwd='123qwe',
    db='djangoblog',
)

# 通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()
print(cur)

# cur.close() 关闭游标
cur.close()

# conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()

# conn.close()关闭数据库连接
conn.close()
