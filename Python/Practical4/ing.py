inpt=input("Enter a word\n>>>")
if len(inpt)<3:
    print("\n",inpt)
elif inpt.endswith("ing") is True:
    print("\n",inpt+"ly")
else:
    print("\n",inpt+"ing")
