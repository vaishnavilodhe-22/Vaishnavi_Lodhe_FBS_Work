# write a program to reverse three digit number
num=int(input("Enter number:"))
rev=0
while num>0:
        ld=num%10
        rev=ld
        num=num//10
        print(rev,end=" ")        