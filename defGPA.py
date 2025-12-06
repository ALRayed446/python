def gp(marks):
    if marks >= 80:
        g = 5
    elif marks >= 70:
        g = 4
    elif marks >= 60:
        g = 3.5
    elif marks >= 50:
        g = 3
    elif marks >= 40:
        g = 2
    elif marks >= 33:
        g = 1
    return g

b1 = int(input("Bangla 1st: "))
b2 = int(input("Bangla 2nd: "))
e1 = int(input("English 1st: "))
e2 = int(input("English 2nd: "))
s = int(input("Sociology: "))
r = int(input("Religion: "))
m = int(input("General Math: "))
i = int(input("ICT: "))

p = int(input("Physics: "))
c = int(input("Chemistry: "))
b = int(input("Biology: "))

h = int(input("Higher Math: "))

if (b1 < 33 or b2 < 33 or e1 < 33 or e2 < 33 or s < 33 or r < 33 or m < 33 or i < 33 or p <= 33 or c < 33 or b < 33):
    print("Sorry,You Are failed.")
else:
    if gp(h) <=2:
        x = gp(b1) + gp(b2) + gp(e1) + gp(e2) + gp(m) + gp(i) + gp(p) + gp(c) + gp(b)
        gpa = x / 9
    elif gp(h) >2:
        x = gp(b1) + gp(b2) + gp(e1) + gp(e2) + gp(m) + gp(i) + gp(p) + gp(c) + gp(b)+gp(h)-2
        if x>=45:
            gpa=5
        elif x<45:
            gpa=x/9

    print("Your GPA is ",gpa)



