units=float(input("Please enter units: "))
if units<0:
    print("Please enter a positive number.")
elif units>0:
    amount=0.5*units
    print("The Bill amount is",amount)
elif units>200:
    amount=100+0.65*units
    print("The Bill amount is",amount)
elif units>400:
    amount=230+0.80*units
    print("The Bill amount is",amount)
else:
    amount=390+1*units
    print("The Bill amount is",amount)
