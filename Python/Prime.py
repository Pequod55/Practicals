import math
while True:
    Input=input("Please enter a number: ")
    try:
        float(Input)
        break
    except:
        print("That was not a number.")
        continue
x=2
y=float(Input)
root=math.sqrt(y)
r=1
while True:
    #print(x)
    #print(root)
    r=y%x
    z=y/x
    if r==0:
        print("The number is not a Prime.")
        break
    elif x>root:
        print("The number is a Prime.")
        break
    else:
        x=x+1
        continue
