# Write a program to input angles of a triangle and check whether triangle is valid or not.
a=int(input("Enter first angle of triangle:"))
b=int(input("Enter second angle of triangle:"))
c=int(input("Enter third angle of triangle:"))
sum=a+b+c
if(sum==180):
    print("Triangle is valid!")
else:
    print("Triangle is not valid!")