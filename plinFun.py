num = int(input("Enter the number: "))

def pali(n):
    sum1=0
    for i in range(1, n + 1):
        original = i
        num1 = 0 
       
     
        while i != 0:
            ld = i % 10
            num1 = ld + (num1*10)
            i = i // 10
        print(num1, end=" ")
        count=0
        if(original==num1):
            print("Palindrom")
            sum1+=1
                
        else:
            print("not palindrome")
    print("palindrome num :-" ,sum1)
    
  
        

pali(num)
