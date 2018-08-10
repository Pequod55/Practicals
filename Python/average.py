print("Please enter 5 percentages to be averaged:")
per1=float(input("1: "))
per2=float(input("2: "))
per3=float(input("3: "))
per4=float(input("4: "))
per5=float(input("5: "))
total=per1+per2+per3+per4+per5
if total>500:
    print("Invalid percentages detected.")
    quit()
avg=total/5
print("%i is the Average of the 5 percentages"%(avg))
