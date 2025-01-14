
def fibonacci(n):
    if n < 2:
        print(n)
    else:
        f =[0]*2
        f[1] = 1
        for i in range(2,n+1):
            f.append(f[i-1] + f[i-2])
        print( f[n])

n = int(input())
fibonacci(n)