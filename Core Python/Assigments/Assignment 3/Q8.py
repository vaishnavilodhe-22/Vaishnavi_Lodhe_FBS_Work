# 

import random
uid='vaisha'
passw='1622'
userid=input("Enter userid:")
pwd=input("Enter password:")
if(uid==userid and pwd==passw):
    rno=random.randint(1000,9999)
    print(rno)
    uno=int(input("Enter captcha:"))
    if(uno==rno):
        print("Success!!")
    else:
        print("Failed!!")
else:
    print("Invalid userid and password...")
