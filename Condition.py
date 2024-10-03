a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))
if(a>b and a>c ):
    if(b>c):
        print("The larger of two number are ",a, b)
        print("Sum of 2 numbers are ",(a+b)/2)
    else:
        print("THe larger of two number are ",a, b )
        print("Sum of 2 numbers are ",(a+c)/2)
elif(b>a and b>c):
    if(a>c):
        print("The larger of two number are",(b+a)/2)
    else:
        print("Sum of 2 numbers are ",(b+c)/2)
else:
    if(b>a):
        print("The larger of two number are",(c+b)/2)
    else:
        print("Sum of 2 numbers are ",(c+a)/2)