# Write a program to swap two numbers without using third variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Numbers before swapping")
print("a=",a)
print("b=",b)
a,b=b,a
print("Numbers after swapping")
print("a=",a)
print("b=",b)
