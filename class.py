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
            print("Type 1 :- To Write")
            print("Type 2 :- To Read")
            print("Type 3 :- To Append")
            print("Type 4 :- To Clear The Data")
            print("Type 5 :- To Exit")
            print("-----------------------------------------------------------")

            op = int(input("Enter the operation : "))
            
            if(op==1):
                ip = input("Enter the commands : ")
                self.write(ip)
                print("-----------------------------------------------------------")
            elif(op==2):
                self.read()
                print("-----------------------------------------------------------")
            elif(op==3):
                ip = input("Enter the commands : ")
                ip = f" {ip}"
                self.append(ip)
                print("-----------------------------------------------------------")
            elif(op==4):
                self.Clear("")
                print("==---------------------------------------------------------")
            else:
                print("You Exited")
                break


obj = operate()
obj.op()
