import math
def DPChange(money,coins):
    MinNumCoins = [0 for i in range(0,money+1)]
    for i in range(1,money+1):
        MinNumCoins[i] = math.inf
        for j in range(0,len(coins)):
            if i>=coins[j]:
                NumCoins = MinNumCoins[ i -coins[j]] + 1
                if NumCoins < MinNumCoins[i]:
                    MinNumCoins[i] = NumCoins
    return MinNumCoins[money]

n = int(input())
print(DPChange(n,[1,3,4]))