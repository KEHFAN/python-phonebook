# coding = utf-8
import pymysql
#连接数据库
database=pymysql.connect(host="localhost",user="root",password="root",
                         db="phonebook",port=3306,charset="utf8")
cur=database.cursor()

print("#1.首先查询数据库")
sql="select * from info"
try:
    cur.execute(sql)
    results=cur.fetchall()
    print("姓名","ID")
    for row in results:
        name=row[0]
        id=row[1]
        print(name,id)
except Exception as e:
    raise e
print("#2.插入数据")
sql_in_name=input("请输入要插入的姓名：")
#sql_in_name=sql_in_name.encode('utf-8')
sql_in_id=input("请输入要插入的ID：")
sql_insert=r"insert into info (name,phone) values ('%s','%s');" % (sql_in_name,sql_in_id)
try:
    cur.execute(sql_insert)
    database.commit()
except Exception as e:
    database.rollback()
print("验证插入")
try:
    cur.execute(sql)
    results=cur.fetchall()
    #print("姓名","ID")
    for row in results:
        name=row[0]
        id=row[1]
        print(name,id)
except Exception as e:
    raise e