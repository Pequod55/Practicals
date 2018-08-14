sidea=float(input("Please enter side a: "))
sideb=float(input("Please enter side b: "))
sidec=float(input("Please enter side c: "))
if sidea+sideb>sidec and sidea+sidec>sideb and sideb+sidec>sidea:
    if sidea==sideb==sidec:
        print("The triangle is equilateral")
    elif (sidea==sideb) or (sidec==sidea) or (sideb==sidec):
        print("The triangle is isoceles")
    else:
        print("The triangle is scalar")
else:
    print("The given sides do not make a triangle.")
