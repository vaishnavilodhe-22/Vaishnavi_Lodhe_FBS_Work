# Write a program to convert days into years,weeks,and days.

day=int(input("Enter number of days:"))
year=day//365
rem_days=day%365
week=rem_days//7
remaining_days=rem_days%7

print("Years:",year)
print("Weeks:",week)
print("Days:",remaining_days)
