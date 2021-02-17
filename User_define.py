x=int(input("Enter the number in row:-"))
y=int(input("Enter the number in column:-"))
matrix=[]

for i in range(x):#for loop for row
    c=[]
    for j in range(y):#for loop for column
        j=int(input("Enter the element in list"+str(i)+" " +str(j)+":-"))
        c.append(j)
    print()
    matrix.append(c)

for i in range(x):
    for j in range(y):
        print(matrix[i][j],end=" ")
    print()
