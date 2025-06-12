l1 = []

n1 = int(input("Enter the number : "))
print("enter the",n1,"number")

for i in range(0,n1):
    n2 = int(input("Enter the num"))
    l1.append(n2)

print(l1)
print("----------------------------------")
sum1 = 0

for i  in l1:
    sum1+=i
print("Sum of list is",sum1)

print("----------------------------------")
sum2 =0
for i  in l1:
    sum2+=i
print("Average of list is",sum1/len(l1))

print("----------------------------------")

l1.sort(reverse=True)

print(l1)
