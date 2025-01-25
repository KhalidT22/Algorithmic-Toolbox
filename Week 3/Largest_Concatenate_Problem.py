from functools import cmp_to_key

import sys

def compare(x1, x2):
    if int(x1 + x2) > int(x2 + x1):
        return 1

    else:
        return -1


def largest_num(n,num):

    l1 = [num[i] for i in range(0, n)]
    l1.sort(key=cmp_to_key(compare), reverse=True)
    return int(''.join(l1))

data = list(sys.stdin.read().split())
n = int(data[0])
num = data[1:]
print(largest_num(n,num))