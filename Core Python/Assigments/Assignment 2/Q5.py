# Write a program to convert time into seconds input hh,min,seconds
hh=int(input("Enter time in hrs:"))
min=int(input("Enter time in min:"))
sec=int(input("Enter time in sec:"))

total_seconds=hh*3600+min*60+sec

print("total seconds are:",total_seconds)