import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "mysqlpython"
    
)

cursor = conn.cursor()
while True:
    op = int(input("Enter the if want to login/signup : "))

    if(op == 1):
        ip = input("Enter the name : ")
        ip1 = input("Enter the age : ")
        sql = ("insert into emp (name,age) values (%s,%s)")
        values = (ip,ip1)
        cursor.execute(sql,values)
    elif(op == 2):
        ip = input("Enter the name : ")
        sql = ("select * from emp where name = %s ")
        cursor.execute(sql,(ip,))
        result = cursor.fetchall()
        if(result):
            print("YOU ARE LOGIN")
        else:
            print("INCORRECT DATA")
    else:
        break

conn.close()
