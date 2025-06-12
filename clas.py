class operations:
    def write(self,ip):
        self.ip = ip
        fp = open("file.txt",'w')
        fp.write(self.ip)
        fp.close()
        print("Data is inserted successfully")
    def read(self):
        fp = open("file.txt",'r')
        data = fp.read()
        print("The data inside the file is :",data)
    def append(self,ip):
        self.ip = ip
        fp = open("file.txt",'a')
        fp.write(self.ip)
        fp.close()
        print("Data is inserted successfully")
    def Clear(self,ip):
        self.ip = ip
        fp = open("file.txt",'w')
        fp.write(self.ip)
        fp.close()
class operate(operations):
    def op(self):
        while True:
            op = int(input("Enter the operation : "))
            if(op==1):
                ip = input("Enter the commands : ")
                self.write(ip)
            elif(op==2):
                self.read()
            elif(op==3):
                ip = input("Enter the commands : ")
                self.append(" "+ip)
            elif(op==4):
                self.Clear("")
            else:
                print("You Exited")
                break


obj = operate()
obj.op()