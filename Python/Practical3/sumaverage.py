n=float(input("Enter n:\n>>>"))
sum=0
average=0
total=n
while n>0:
    sum=sum+n
    n=n-1
average=sum/total
print("The Sum of numbers till {0} is:\n{1}\nThe Average of numbers till {0} is:\n{2}".format(total,sum,average))
