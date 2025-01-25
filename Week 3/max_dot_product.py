import sys

def max_dot_product(n,prices,clicks):
    sum = 0
    price = sorted(prices, key=lambda x: x, reverse=True)
    clicks = sorted(clicks, key=lambda x: x, reverse=True)
    for i in range(0, n):
        sum += price[i] * clicks[i]
    return sum

data = list(map(int, sys.stdin.read().split()))
n = data[0]
prices = data[1:n+1]
clicks = data[n+1:]
print(max_dot_product(n,prices,clicks))