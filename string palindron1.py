a=input("Enter a string:")
b=int(len(a))
c=""
d=a[0]
for i in range(b-1,0,-1):
    c = c + a[i]
c=c+d
print(c)