
for i in range(0,6):
    for u in range(6,i,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print("=", end =" ")
    for u in range(1,i):
        print("=", end =" ")
        
    print()
for i in range(0,6):
    for u in range(0,i):
        print(" ",end="")
    for j in range(6,i,-1):
        print("=", end =" ")
    for u in range(5,i,-1):
        print("=", end =" ")
        
    print()
 
