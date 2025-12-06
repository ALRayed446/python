while True:
    n = int(input("Please Enter a Number (enter 0 to exit): "))

    p = 0
    if n == 0:
        break

    if n == 1:
        print("1 is not a prime number")
        continue

    for i in range(2, n):
        if n % i == 0:

            p = 1
            break

    if p == 0:
        print(n, "is a PRIME NUMBER")
    else:
        print(n, "is NOT a PRIME NUMBER")