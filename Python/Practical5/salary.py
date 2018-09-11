x=1
salary=[]
print("To find Maximum Salary enter the salary as 0")
while x>0:
    inpt=float(input("Enter salary of an employee: "))
    salary.append(inpt)
    if inpt==0:
        break
salary.sort(reverse=True)
print(salary[0])
