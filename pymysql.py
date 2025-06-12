import pymysql as py

conn = py.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='yourdatabase'
)

print(myconn)
