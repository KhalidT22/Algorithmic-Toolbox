def fibonacci_partial_sum(m,n):
    m = int(m)
    n = int(n)

    if n < 2:
        return n
    else:
        f_n1 = 1
        f_n2 = 0
        if m <= 1 :
            sum =1
        else:
            sum = 0
        m = m % 60
        n = n % 60
        if n < m:
            n += 60

        for i in range(2,n+1):
            f_n = f_n1 +f_n2
            if i >= m:
                sum += f_n
            f_n2 = f_n1
            f_n1 = f_n
        return sum%10

m,n = input().split()
print(fibonacci_partial_sum(m,n))


