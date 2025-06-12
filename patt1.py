num = int(input("Enter the Number 1 to Sign up or 2 to Login :- "))

if(num == 1):
    print("Sign up :- ")
    name = input("Enter the name :- ")
    user = input("Enter the username :- ")
    pas = input("Enter the password :- ")
    print("Name is :- ",name)
    print("Username is :- ",user)
    print("Password is :- ",pas)
elif(num== 2):
    print("Login :- ")
    user = input("Enter the username :- ")
    pas = input("Enter the password :- ")
    print(pas,user)
else:
    for i in range(0,num):
        print("Invalid Input",i)
    
