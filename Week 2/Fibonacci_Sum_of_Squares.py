def fibonacci_sum_of_squares(n):
    n = n % 60
    if n < 2:
        return n
    else:
        f_n1 = 1
        f_n2 = 0
        for i in range(2,n+2):
            f_n = f_n1 +f_n2
            f_n2 = f_n1
            f_n1 = f_n
        return (f_n*f_n2)%10


n = int(input())
print(fibonacci_sum_of_squares(n))