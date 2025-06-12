class operation:

       
    def write(self,ip):
        self.ip = ip
        fp = open("file.txt",'w')
        fp.write(ip)
        fp.close()
        print("Data inserted Successfully")
    def read(self):
        fp = open("file.txt",'r')
        fp.read()
        fp.close()
ip = input("Enter the commands : ")
class operate(operation):
    def op1(self,op):
        self.op = op
        while True:
            if(self.op == 1):
                
                self.write(ip)
            elif(self.op == 2):
                self.read()

op = int(input("Enter the task : "))
obj = operate()
obj.op1(op)