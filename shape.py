import module as m

Shape = input("Enter the shape (Circle,rectangle,square): ")

op = input("Enter the operation (area,perimeter,diagonal/diameter): ")

if(Shape == 'rectangle'):
    num1 = int(input("Enter the length : "))
    num2 = int(input("Enter the breadth : "))
    if(op=='area'):
        m.recta(num1,num2)
    elif(op=='perimeter'):
        m.rectp(num1,num2)
    elif(op=='diagonal'):
        m.rectd(num1,num2)
    else:
        print("Invalid")
elif(Shape == 'square'):
    num1 = int(input("Enter the side : "))
    if(op=='area'):
        m.sqa(num1)
    elif(op=='perimeter'):
        m.sqp(num1)
    elif(op=='diagonal'):
        m.sqd(num1)
    else:
        print("Invalid")
elif(Shape == 'circle'):
    num1 = int(input("Enter the radius : "))
    if(op=='area'):
        m.circleA(num1)
    elif(op=='perimeter'):
        m.circleP(num1)
    elif(op=='diameter'):
        m.circleD(num1)
    else:
        print("Invalid")
