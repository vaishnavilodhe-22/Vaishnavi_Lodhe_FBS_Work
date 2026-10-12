# write a program to calculate area of triangle and rectangle

l=int(input("Enter lenght:"))
b=int(input("Enter breadth:"))

base=int(input("Enter base:"))
height=int(input("Enter height:"))

A_rect=l*b
A_tri=0.5*base*height

print("Area of rectangle:",A_rect)
print("Area of triangle:",A_tri)