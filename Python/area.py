shape=input("Please enter the shape you want to fint he area of (square, rectangle, circle or rhombus): ")
if shape=="square":
    side=float(input("Enter the length of the side of the square(in cm): "))
    area=side**2
    print("%i sq.cm is the area of the sqaure."%(area))
    quit()
if shape=="rectangle":
    length=float(input("Enter the length of the side of the rectangle(in cm): "))
    breadth=float(input("Enter the breadth of the side of the square(in cm): "))
    area=length*breadth
    print("%i sq.cm is the area of the rectangle."%(area))
    quit()
if shape=="circle":
    radius=float(input("Please enter the radius of the circle: "))
    area=3.14*radius
    print("%i sq.cm is the area of the circle."%(area))
if shape=="rhombus":
    diagonal1=float(input("Please enter the length of the first diagonal: "))
    diagonal2=float(input("Please enter the length of the second diagonal: "))
    area=(diagonal1*diagonal2)/2
    print("%i sq.cm is the area of the rhombus."%(area))
