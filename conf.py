import pymssql
# 连接数据库
conn = pymssql.connect("数据库地址","用户名","密码","数据库名")
db = conn.cursor()
