sum=0
for i in range(2,101):
    for j in range(2,i-1):
        print(j)
        print("\t",i)
        if i%j==0:
            break
    else:
            sum=sum+i
print(sum)
