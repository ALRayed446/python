while True:
    fib_x = 0
    fib_y = 1
    n = int(input("Enter n: "))
    if n <= 0:
        print("Invalid input")
    else:
        for i in range(n):
            print(fib_x)

            fib_temp = fib_x + fib_y
            fib_x = fib_y
            fib_y = fib_temp
            t = (fib_y / fib_x)
            print("Fibonacci ratio: ", t )
