def palindron(num):
    int(num)
    count = 0
    n = abs(num)

    if n == 0:
        count = 1
    else:
        while n > 0:
            n //= 10
            count += 1

    temp = abs(num)
    b = 0

    for i in range(count):
        x = temp % 10
        temp = temp // 10
        b = b + x * 10 ** (count - i - 1)
    return b
print(palindron(123))
print(palindron(412332342))
print(palindron(63476658))
