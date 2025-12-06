def palindrom(a):
    a=a.lower()
    b = int(len(a))
    c = ""
    for i in range(b - 1, -1, -1):
        c = c + a[i]

    if a == c:
        print("Palindrom")
    else:
        print("Not Palindrom")

palindrom(input("Enter The word:  "))