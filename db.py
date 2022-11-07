import pymysql as p
def connect():
    return p.connect(host="localhost",user="root",password="",database="Primetime",port=3306)

def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into details values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
def check(email):
    con=connect()
    cur=con.cursor()
    sql="select email,Choose_password from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def userdata():
    con=connect()
    cur=con.cursor()
    sql="select * from details"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
    
def single_user(email):
    con=connect()
    cur= con.cursor()
    sql="select * from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0]

