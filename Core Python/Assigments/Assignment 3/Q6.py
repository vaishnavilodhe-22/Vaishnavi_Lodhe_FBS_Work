# Write a program to calculate profit or loss.
sp=int(input("Enter selling price:"))
cp=int(input("Enter cost price:"))
profit=sp-cp
loss=cp-sp
if(sp>cp):
    print("profit is",profit)
else:
    print("Loss is",loss)    
