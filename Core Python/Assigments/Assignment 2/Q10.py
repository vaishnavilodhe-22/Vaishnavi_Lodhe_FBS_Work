# Wriet a program to calculate total salary of employee based on basic da=10%
# of basic ta=12% of basic and hra=15% of basic

basic=int(input("Enter basic salary:"))
da=basic*10/100
hra=basic*12/100
ta=basic*15/100
total_sal=da+hra+ta
print("Total salary :",total_sal)

