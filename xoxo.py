a=int(input("enter the number"))
for i in range(a):
    for j in range(a):
        if (i+j)%2==0:
            print("x",end=" ")
        else:
            print("o",end=" ")
    print()


