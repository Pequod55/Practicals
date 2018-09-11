row=int(input("Enter rows of matrices: "))
column=int(input("Enter column of matrices: "))
mat1=[]
mat2=[]
mat3=[]
num1=0
y=0
x=row*column
z=x
print("ENTER 1ST MATRIX")
if column>row:
    while x>0:
        for i in range(1,column+1):
            for j in range(1,row+1):
                print("\nEnter the digit in Column {0} Row {1}:  ".format(i,j))
                num1=int(input(">>>"))
                mat1.append(num1)
                x=x-1
                y=1
else:
    while x>0:
        for i in range(1,row+1):
            for j in range(1,column+1):
                print("\nEnter the digit in Row {0} Column {1}:  ".format(i,j))
                num1=int(input(">>>"))
                mat1.append(num1)
                y=0
                x=x-1
print("ENTER 2ND MATRIX")
x=z
if y==1:
    while x>0:
        for i in range(1,column+1):
            for j in range(1,row+1):
                print("\nEnter the digit in Column {0} Row {1}:  ".format(i,j))
                num2=int(input(">>>"))
                mat2.append(num2)
                x=x-1
                y=1
if y==0:
    while x>0:
        for i in range(1,row+1):
            for j in range(1,column+1):
                print("\nEnter the digit in Row {0} Column {1}:  ".format(i,j))
                num2=int(input(">>>"))
                mat2.append(num2)
                y=0
                x=x-1
print("\n\n")
lambai=len(mat1)
for i in range(lambai):
    tot=mat1[i]+mat2[i]
    mat3.append(tot)

i=0
for j in range(column):
    print("| ",end="")
    for k in range(row):
        print(mat1[i],end=" ")
        i=i+1
    print("|")
print("   +")
i=0
for j in range(column):
    print("| ",end="")
    for k in range(row):
        print(mat2[i],end=" ")
        i=i+1
    print("|")
print("   =")
i=0
for j in range(column):
    print("| ",end="")
    for k in range(row):
        print(mat3[i],end=" ")
        i=i+1
    print("|")
