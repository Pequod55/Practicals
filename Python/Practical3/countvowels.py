inpt=input("Enter a string\n>>>")
inpt=inpt.lower()
acount=ecount=icount=ocount=ucount=0
print(inpt)
for i in inpt:
    if i=="a":
        acount=acount+1
    elif i=="e":
        ecount=ecount+1
    elif i=="i":
        icount=icount+1
    elif i=="o":
        ocount=ocount+1
    elif i=="u":
        ucount=ucount+1
print("\nCount of Vowels:\nA: {0}\nE: {1}\nI: {2}\nO: {3}\nU: {4}".format(acount,ecount,icount,ocount,ucount))
