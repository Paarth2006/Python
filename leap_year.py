print("\t\t*****INPUT*****")
year = int(input("Enter the Year:"))
print("\t\t*****OUTPUT*****")
if (year % 400 == 0) or (year % 4 == 0) and (year % 100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")