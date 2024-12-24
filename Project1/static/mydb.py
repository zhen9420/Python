import pymysql

conn = pymysql.connect(host='127.0.0.1',  # 连接主机, 默认127.0.0.1
                       user='root',  # 用户名
                       passwd='123456',  # 密码
                       port=3306,  # 端口，默认为3306
                       db='educ',  # 数据库名称
                       charset='utf8'  # 字符编码
                       )

#千万不要用字符串格式化做sql的拼接，以防sql注入


sql = "insert into course(cno,cname,cpno,Ccredit) values (%s,%s,%s,%s)"

cursor = conn.cursor()

cursor.execute(sql, ["9","python",None,"3"])

conn.commit()

cursor.close()
conn.close()
