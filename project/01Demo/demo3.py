#查询数据库
import pymysql

#查询MYSQL
'''
conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
cur = conn.cursor()
sql = "select * from con_map"
cur.execute(sql)
# result = cur.fetchone()
result = cur.fetchall()
print(type(result))
print(result)
for data in result:
    print(data)
cur.close()
conn.close()
'''



#数据插入MYSQL
conn = pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='123456',charset='utf8')
cur = conn.cursor()
try:
    sql = "insert into con_map(CON_HPYS,CON_HPHM) values('黄蓉','80')"
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
    print('插入信息错误')
    raise
finally:
    cur.close()
    conn.close()

