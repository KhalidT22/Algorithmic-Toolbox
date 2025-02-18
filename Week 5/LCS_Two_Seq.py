

import sys
data = list(sys.stdin.read().split())
n = int(data[0])
a = data[1:n+1]

b = data[n+2:]


def LCS_2_seq(a,b):
    lcs = [[0] * (len(b) + 1) for j in range(0, len(a) + 1)]
    a1 = [0]
    b1 = [0]
    a1.extend(a)
    b1.extend(b)
    for j in range(1,len(a)+1):
        for i in range(1,(len(b) + 1) ):
            if a1[j] == b1[i]:
                lcs[j][i] = 1 + lcs[j-1][i-1]
            else:
                lcs[j][i] = max(lcs[j-1][i],lcs[j][i-1])
    return  lcs[len(a)][len(b)]

print(LCS_2_seq(a,b))