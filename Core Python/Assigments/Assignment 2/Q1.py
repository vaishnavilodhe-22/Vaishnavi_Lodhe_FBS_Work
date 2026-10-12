# Write a program to find sum of three digit
num=int(input("Enter number:"))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum of digit is",sum)
