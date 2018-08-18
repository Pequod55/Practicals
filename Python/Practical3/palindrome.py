inpt=input("Enter a string or number: ")
lst=[]
for i in inpt:
    lst.append(i)
lst.reverse()
revinpt=None
for i in lst:
    if revinpt==None:
        revinpt=i
        continue
    revinpt=revinpt+i
if inpt==revinpt:
    print("Given number or string is a palindrome.")
else:
    print("Given number or string is not a palindrome.")
