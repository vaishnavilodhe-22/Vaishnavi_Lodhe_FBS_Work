# Write a program to calculate selling price of book based on cost price and discount

cost_p=int(input("Enter cost price of book:"))
discount=int(input("Enter discount:"))
dis=cost_p*discount/100
selling_p=cost_p-dis
print("selling price",selling_p)
