#coding = utf-8
import pymysql

#查询所有联系人
def ListAll():
    sql_sel_all="select * from info;"
    cur=database.cursor()
    try:
        cur.execute(sql_sel_all)
        results=cur.fetchall()
        print("姓名","电话","邮箱","住址")
        for row in results:
            name=row[0]
            phone=row[1]
            mail=row[2]
            address=row[3]
            print(name,phone,mail,address)
    except Exception as e:
        raise e
    cur.close()

#添加联系人
def InsertInfo(name,phone,mail=None,address=None):
    sql_insert=r"insert into info (name,phone," \
               r"mail,address) values ('%s','%s','%s'," \
               r"'%s');" % (name,phone,mail,address)
    cur=database.cursor()
    try:
        cur.execute(sql_insert)
        database.commit()
    except Exception as e:
        database.rollback()
    cur.close()

#删除联系人
def DeleteInfo(name,phone):
    sql_delete=r"delete from info where name='%s' " \
               r"and phone='%s';" % (name,phone)
    cur=database.cursor()
    try:
        cur.execute(sql_delete)
        database.commit()
    except Exception as e:
        database.rollback()
    cur.close()

"""
if __name__=="__main__":
    database = pymysql.connect(host="localhost", user="root", password="root",
                               db="phonebook", port=3306, charset="utf8")
    ListAll()
    
    ListAll()

    database.close()
"""