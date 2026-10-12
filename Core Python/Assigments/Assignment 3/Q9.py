# Input 5 subject marks from user and display grade.
m1=int(input("Enter marks of sub1:"))
m2=int(input("Enter marks of sub2:"))
m3=int(input("Enter marks of sub3:"))
m4=int(input("Enter marks of sub4:"))
m5=int(input("Enter marks of sub5:"))
total=m1+m2+m3+m4+m5
per=total/5
if(per>=90):
    print("First class.")
elif(per>=70 and per<=90):
    print("Second class.")
elif(per>=35 and per<=70):
    print("Passed.")
else:
    print("Failed..")
  

