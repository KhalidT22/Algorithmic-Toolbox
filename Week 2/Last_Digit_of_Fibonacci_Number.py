
def last_digit_fibonacci(n):
    if n < 2:
        print(n)
    else:
        num = n % 60
        f =[0]*2
        f[1] = 1
        for i in range(2,num+1):
            f.append(f[i-1] + f[i-2])
        print( f[num] % 10)



n = int(input())
last_digit_fibonacci(n)
