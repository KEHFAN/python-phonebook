import tkinter
import pymysql
from tkinter import *
from tkinter import  ttk
window=tkinter.Tk()#创建窗口

window.title("电话簿")#设置标题
window.geometry('500x500+500+200')#设置大小偏移量
window.resizable(width=False,height=False)#禁用宽高
database = pymysql.connect(host="localhost", user="root", password="root",
                               db="phonebook", port=3306, charset="utf8")

ListN=ttk.Treeview(window)
ListN=ttk.Treeview(window,show="headings",height=10,columns=("a","b","c","d"))
#ListN["columns"]=("a","b","c","d")
ListN.column("a",width=60)
ListN.column("b",width=100)
ListN.column("c",width=120)
ListN.column("d",width=200)
ListN.heading("a",text="姓名")
ListN.heading("b",text="电话")
ListN.heading("c",text="邮箱")
ListN.heading("d",text="住址")
ListN["selectmode"]="browse"
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
def ListAll():
    sql_sel_all="select * from info;"
    cur=database.cursor()
    try:
        cur.execute(sql_sel_all)
        results=cur.fetchall()
        #print("姓名","电话","邮箱","住址")

        #首先删除表格中的原节点数据
        for _ in map(ListN.delete,ListN.get_children("")):
            pass

        ii=0
        for row in results:
            name=row[0]
            phone=row[1]
            mail=row[2]
            address=row[3]
            #print(name,phone,mail,address)
            ListN.insert("",ii,text=ii+1,values=(name,phone,mail,address))
            ii=ii+1
    except Exception as e:
        raise e
    cur.close()
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
def Nodes():
    notenote1="说明："
    notenote2="     添加联系人时至少输入姓名和电话"
    notenote3 ="     邮箱和住址可以省略，可以添加同名"
    notenote4 ="     但不能添加同名，同电话的信息"
    notenote5 ="删除时只需选中要删除的项，然后点击"
    notenote6 ="删除联系人按钮即可删除"
    note1=Label(window,text=notenote1)
    note1.pack()
    Label(window,text=notenote2).pack()
    Label(window,text=notenote3).pack()
    Label(window,text=notenote4).pack()
    Label(window,text=notenote5).pack()
    Label(window,text=notenote6).pack()
    pass
#创建子窗口
def zwindow():

    zwin = tkinter.Tk()
    zwin.title("添加")
    zwin.geometry('350x200+520+350')
    zwin.resizable(width=False,height=False)
    Ln=Label(zwin,text="姓名")
    Lp=Label(zwin,text="电话")
    Lm=Label(zwin,text="邮箱")
    La=Label(zwin,text="地址")
    Ln.grid(row=0)
    Lp.grid(row=1)
    Lm.grid(row=2)
    La.grid(row=3)
    e1=Entry(zwin)
    e2=Entry(zwin)
    e3=Entry(zwin)
    e4=Entry(zwin)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)

    def InsertI():
        InsertInfo(e1.get(), e2.get(), e3.get(), e4.get())
        zwin.destroy()
        ListAll()
    YButton=Button(zwin,text='确定',command=InsertI)
    NButton=Button(zwin,text='取消',command=zwin.destroy)
    YButton.grid(row=4,column=1,padx=3)
    NButton.grid(row=4,column=2)
def Delete():
    #ListN.
    items=ListN.selection()#返回被选中行的ID
    Delete_name=ListN.item(items)["values"][0]
    Delete_phone=ListN.item(items)["values"][1]
    #print(items)
    #print(ListN.item(items))
    #print(Delete_name)
    #print(Delete_phone)
    DeleteInfo(Delete_name,Delete_phone)
    ListAll()
    pass
InsertB=Button(window,text='添加联系人',command=zwindow)
DeleteB=Button(window,text='删除联系人',command=Delete)
ListAll()
ListN.pack()
InsertB.pack()
DeleteB.pack()
Nodes()
window.mainloop()


