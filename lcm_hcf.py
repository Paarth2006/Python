print("\t\t*****INPUT*****")
x = int(input("Enter 1st Number:"))
y = int(input("Enter 2nd Number:"))
gcd = 1
for i in range(1,min(x,y)):
    if (x%i==0) and (y%i==0):
        gcd = i
lcm = (x*y)//gcd
print("\t\t*****OUTPUT*****")
print("GCD of",x,"and",y,"is :",gcd)
print("LCM of",x,"and",y,"is :",lcm)
