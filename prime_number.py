n=int(input("Enter a Number:"))
def primenumber(n):
    c=0
    for i in range(2,n):
        if n%i == 0:
            c+=1
    if c!=0:
        print(n,"is a Composite Number")
    else:
        print(n,"is a Prime Number")
primenumber(n)