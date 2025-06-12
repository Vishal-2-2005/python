import mysql.connector as mydb


conn = mydb.connect(
    host="localhost",
    user="root",
    password="root",
    database="mysqlpython"
)
cur = conn.cursor()

class Operation:
    def insert(self):
        ip = input("Enter the first name: ")
        ip1 = input("Enter the last name: ")
        sql = "INSERT INTO mysql (name, last) VALUES (%s, %s)"
        values = (ip, ip1)
        cur.execute(sql, values)
        conn.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def delete(self):
        ip = input("Enter the name to delete: ")
        sql = "DELETE FROM mysql WHERE name=%s"
        values = (ip,)
        cur.execute(sql, values)
        conn.commit()  # Commit the deletion
        print("DATA DELETED SUCCESSFULLY")

    def update(self):
        op = input("Enter what we have to update (name/lastname): ").lower()
        if op == 'name':
            old_name = input("Enter the current name: ")
            new_name = input("Enter the new name: ")
            sql = "UPDATE mysql SET name = %s WHERE name = %s"
            values = (new_name, old_name)
        elif op == 'lastname':
            old_lastname = input("Enter the current last name: ")
            new_lastname = input("Enter the new last name: ")
            sql = "UPDATE mysql SET last = %s WHERE last = %s"
            values = (new_lastname, old_lastname)
        else:
            print("Invalid option!")
            return
        
        cur.execute(sql, values)
        conn.commit()  # Commit the update
        print("DATA UPDATED SUCCESSFULLY")

    def fetch(self):
        cur.execute("SELECT * FROM mysql")
        result = cur.fetchall()
        for row in result:
            print(row)


class Operates(Operation):
    def ops(self):
        while True:
            print("\n1. Insert\n2. Delete\n3. Update\n4. Fetch\n5. Exit")
            op = int(input("Enter the operation: "))
            if op == 1:
                self.insert()
            elif op == 2:
                self.delete()
            elif op == 3:
                self.update()
            elif op == 4:
                self.fetch()
            else:
                print("Exiting...")
                break


obj = Operates()
obj.ops()
