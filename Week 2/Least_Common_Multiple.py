def GCD(x):
    num = x.split()
    a = int(num[0])
    b = int(num[1])
    if a == 0:
        return b
    else:
        y = str(b%a)+" "+str(a)
        return GCD(y)

def LCM(x):
    num = x.split()
    a = int(num[0])
    b = int(num[1])
    return int(abs(a)*(abs(b)/GCD(x)))


x=  input()
print(LCM(x))