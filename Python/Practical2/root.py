a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
if a==0 and b==0 and c!=0:
    print("There is no solution.")
elif a==0:
    print("There is only one root.")
    X=-c/b
    print("x=",X)
elif b**2-4*a*c<0:
    print("There are no real roots.")
else:
    print("There are two real roots:/n")
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print("X1= ",x1)
    print("\nX2=",x2)
