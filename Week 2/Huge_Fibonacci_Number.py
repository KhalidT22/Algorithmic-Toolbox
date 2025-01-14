def fibonacci(n):
    if n < 2:
        return n
    else:
        f_n1 = 1
        f_n2 = 0
        for i in range(2,n+1):
            f_n = f_n1 + f_n2
            f_n2 = f_n1
            f_n1 = f_n
        return f_n

def pisano(m):
    prev_elm = 0
    cur_elm = 1
    for i in range(0,m*m+1):
        next_elm = (prev_elm + cur_elm) % m
        prev_elm = cur_elm
        cur_elm = next_elm
        if(cur_elm == 1) & (prev_elm == 0):
            return i+1

def huge_fib(n,m):
    n = int(n)
    m = int(m)
    len_m = pisano(m)
    n = n % len_m
    return fibonacci(n) % m

n,m = input().split()

print(huge_fib(n,m))
