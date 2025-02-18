





import sys
data = list(sys.stdin.read().split())
a = data[0]
b = data[1]

def edit_distance(a,b):
    D =  [ [0]*(len(b)+1) for j in range(0,  len(a) + 1) ]

    for i in range(len(a)+1):
        D[i][0] = i

    for j in range(len(b)+1):

        D[0][j] = j

    a1 = " "+a
    b1 = " "+b

    for j in range(1,len(b)+1):

        for i in range(1,len(a)+1):

            ins = D[i][j-1] +1
            deletion = D[i -1][j]+1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] +1
            if a1[i] == b1[j]:
                D[i][j] = min(ins,deletion,match)
            else:
                D[i][j] = min(ins, deletion, mismatch)

    return D[len(a)][len(b)]
print(edit_distance(a,b))
