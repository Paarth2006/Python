print("\t\t*****INPUT*****")
x = int(input("Enter the X Coordinate :"))
y = int(input("Enter the Y Coordinate:"))
print("\t\t*****OUTPUT*****")
if x>0 and y>0:
    print((x,y),"lies in First Quadrant")
if x<0 and y>0:
    print((x,y),"lies in Second Quadrant")
if x<0 and y<0:
    print((x,y),"lies in Third Quadrant")
if x>0 and y<0:
    print((x,y),"lies in Fourth Quadrant")