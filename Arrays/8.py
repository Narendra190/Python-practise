a=int(input("Enter the first side of triangle: "))
b=int(input(   "Enter the second side of triangle: "))
c=int(input(    "Enter the third side of triangle: "))
if(((a+b)>c) and ((b+c)>a) and ((c+a)>b)):
    if (a==b==c):
        print("equlateral triangle")
    elif((a==b) or (b==c) or (c==a)):
        print("isoscale triangle")
    else:
        print("scalane triangle")
else:
    print("not a valid triangle")