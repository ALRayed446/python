a=int(input("enter number:"))

for i in range(1,a+1):
    print("*"*(a-i)+"  "*i,"*"*(a-i)+"  "*i)
for j in range(a,0,-1):
    print("*"*(a-j)+"  "*j,"*"*(a-j)+"  "*j)
