# write a program to convert given distance into centimeter and meters
feet=int(input("Enter Distance in feet:"))
inches=int(input("Enter distance in inches:"))

inch=feet*12
total_inches=inch+inches
total_centimeter=total_inches*2.54
remaining_centimeter=total_centimeter%100
meter=total_centimeter/100
print("Centimeter is",total_centimeter)
print("Meter is",meter)