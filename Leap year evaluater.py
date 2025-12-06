y=int(input("YEAR: "))
if ((y%400==0 and y%100==0)or(y%100!=0 and y%4==0)):
    print("leap year")
else:
    print("Not a leap year")