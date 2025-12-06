def fibbonacci(n):
    n=n-1
    fib_x = 0
    fib_y = 1
    if n <= 0:
        print("Invalid input")
    else:
        for i in range(n):


            fib_temp = fib_x + fib_y
            fib_x = fib_y
            fib_y = fib_temp
        print(fib_x)
fibbonacci(10)
