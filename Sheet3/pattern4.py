n=int(input("Enter the number:"))
for i in range(n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()