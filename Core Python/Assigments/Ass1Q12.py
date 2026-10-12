# Write a program to find the roots of quadtratic equation.

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

d=(b**2-4*a*c)*0.5

x1=-b-d/2*a*c
x2=-b+d/2*a*c

print("x1 root is:",x1)
print("x2 root is:",x2)