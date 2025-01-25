def covering_segment(seq):
    list = []
    while len(seq) > 0:
        seq = sorted(seq, key=lambda x: x[1])
        #print("Seq: ",seq)
        cur_point = seq.pop(0)
        max = cur_point[0]
        #print("cur_point: ", cur_point)
        index = []
        for i in range(0, len(seq)):
            if seq[i][0] <= cur_point[1]:
                index.append(i)
                if seq[i][0] >= max:
                    max = seq[i][0]
        #print("max: ", max)
        list.append(max)
        index = sorted(index, key=lambda x: x, reverse=True)
        for i in index:
            seq.pop(i)

    return list

import sys
data = list(map(int, sys.stdin.read().split()))

n = data[0]
k = 0
seq = []
for i in range(0,n):

    seq.append( ( data[k+1] , data[k+2]))
    k += 2

list = covering_segment(seq)
print(len(list))
print(" ".join(map(str,list)))