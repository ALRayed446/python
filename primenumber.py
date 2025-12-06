while True:
    n1 = int(input("Please Enter Starting Range: "))
    n2 = int(input("please Enter Ending Range: "))

    if n1 == 0 or n2 == 0:
        break
    for n in range(n1, n2 + 1):
        p = 0
        if n == 1:
            continue
        for i in range(2, n):
            if n % i == 0:
                p = 1
                break
        if p == 0:
            print(n, "is a PRIME NUMBER")