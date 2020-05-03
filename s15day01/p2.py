#coding:utf-8
from pyhdfs import HdfsClient
client = HdfsClient(hosts='192.168.111.134:50070')  #50070是端口号
print(client.list_status('/'))   #打印
client.copy_from_local("cloud","/test.txt")
import happybase
# connection = happybase.Connection('localhost')
# connection.open()
#
# # xxx 表示表名，在连接之前要先在终端创建表
# ## table = conn.table("table01")
#
# # 创建表---> zhy为表名，info为指定行列为空
# conn.create_table('table01', {"info":{}})
#
# # 删除表--> disable默认为False，删除表的手要修改为True
# conn.delete_table("testtest", True)

# conn = happybase.Connection("192.168.111.134",9090)
# conn.create_table('table02', {"info":{}})

# table = conn.table("table01")
#
# table.put("table01",{"info:data":"22222"})
# row = table.row("table01")
# print(row)


# import happybase
#
# # 连接
# connection = happybase.Connection('192.168.111.129')
# connection.open()
#
# # connection.create_table('mytable', {'name' : dict(max_versions=5), 'course':dict()})
# # 打印所有的表
# print(connection.tables())
# table = connection.table('Score')
# row = table.row(b'95001')
# print(row[b'course:Math'])
#
# # 插入数据
# table.put(b'95002', {b'course:Math': b'65', b'course:English': b'77'})

# 19095










