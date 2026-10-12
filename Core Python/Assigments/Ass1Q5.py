# Q5.Write a program to P,T,R and calculate compound intrest
p=int(input("Enter principle amount:"))
T=int(input("Enter year in time:"))
R=int(input("Enter intrest rate:"))
amt=p*1+R/100**T
CI=amt-p
print("compound intrest:",CI)