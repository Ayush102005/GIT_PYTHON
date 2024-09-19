#Write a Python Program to get 3 Subject Marks Out of that find average for biggest of two subject marks.
a=float(input("Enter The Marks A: "))
b=float(input("Enter The Marks B: "))
c=float(input("Enter the Marks C: "))
sum=0
if a>c and b>c:
    sum=a+b
if b>a and c>a:
    sum=b+c
if a>b and c>b:
    sum=a+c
print("Avg:",sum/2)