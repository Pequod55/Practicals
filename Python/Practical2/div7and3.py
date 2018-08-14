num=float(input("Please enter a number: "))
if num%3==0:
    if num%7==0:
        print("The number is divisible by 3 and 7")
    else:
        print("The given number is divisible by 3 only")
if num%7==0:
    print("The number is only divisible by 7")
