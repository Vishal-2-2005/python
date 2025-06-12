f = open("hello.txt",'r')
ip = input("Enter  : ")
data = f.read()
c =  ""
li = []
for i in data:
    c+=i
    if(i == ""):
        li.append(c)
        c = ''
print(li)