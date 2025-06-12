import mysql.connector as mydb

myconn=mydb.connect(
    host="localhost",
    user="root",
    password="root",
    database = "Vishal123"
)
# mycursor = myconn.cursor()

# # mycursor.execute("create table emp (name varchar(255),last varchar(255))")
# # myconn.close()
# # print(myconn)
# sql = ("insert into emp(name,last) values(%s,%s)")
# values = ("v","b")
# mycursor.execute(sql,values)
# myconn.commit()
# myconn.close()
print(myconn)