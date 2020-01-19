import random
list = []
for i in range(0,200):
    list.append((i,''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))))
for j,k in list:
    print(j,k)
import pymysql

# 打开数据库连接
db = pymysql.connect('127.0.0.1', 'root', '123456', "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
try:
    # 执行sql语句
    cursor.executemany("insert into shopcard(id,card) values(%s,%s)",list)
    # 提交到数据库执行
    db.commit()

except:
    # 如果发生错误则回滚
    db.rollback()
    print("发生错误")
# 使用 fetchone() 方法获取单条数据.

# 关闭数据库连接
db.close()