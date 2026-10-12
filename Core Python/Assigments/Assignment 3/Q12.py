num=int(input("Enter three digit number:"))
no=num
rev=0
while num>0:
    id=num%10
    rev=rev*10+id
    num=num//10
if(no==rev):
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")
