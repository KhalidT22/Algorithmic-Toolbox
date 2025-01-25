def money_change(n):
    num = 0


    while n > 0:
        if n >= 10:
            num += (n // 10)
            n = n - 10 * (n // 10)
        elif n >= 5:
            num += (n // 5)
            n = n - 5 * (n // 5)
        else:
            num += n
            n = 0
    return num

n=int(input())
print(money_change(n))