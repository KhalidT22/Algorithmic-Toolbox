
n = int(input())

def fibonacci_sum(n):
    n = n % 60
    if n > 2:
        f_n1 = 1
        f_n2 = 0
        sum = 1
        for i in range(2, n + 1):
            f_n = f_n1 + f_n2
            sum += f_n
            f_n2 = f_n1
            f_n1 = f_n
        return sum % 10
    else:
        return n

print(fibonacci_sum(n))