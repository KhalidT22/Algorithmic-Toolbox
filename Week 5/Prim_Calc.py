import math
def Prim_Calc(n):
    NumOp = 0
    if n < 4:
        Num_Op_List = [0 for i in range(0, 3)]

    else:
        Num_Op_List = [0 for i in range(0, n + 1)]

    mapping = {}
    mapping[1] = "1"
    mapping[2] = "1 2"
    mapping[3] = "1 3"
    cur_num = 1
    Num_Op_List[1] = 1
    Num_Op_List[2] = 1
    choose = 1
    min_num = 0
    for i in range(4, n + 1):
        min_num = [math.inf, math.inf, math.inf]
        if i % 3 == 0:
            min_num[2] = Num_Op_List[int((i / 3) - 1)] + 1
        if i % 2 == 0:
            min_num[1] = Num_Op_List[int((i / 2) - 1)] + 1
        min_num[0] = Num_Op_List[i - 2] + 1

        choose = min_num.index(min(min_num))
        if choose == 2:
            Num_Op_List[i - 1] = Num_Op_List[int((i / 3) - 1)] + 1
            mapping[i] = mapping[int((i / 3))] + " " + str(i)
        elif choose == 1:
            Num_Op_List[i - 1] = Num_Op_List[int((i / 2) - 1)] + 1
            mapping[i] = mapping[int((i / 2))] + " " + str(i)
        else:
            Num_Op_List[i - 1] = Num_Op_List[i - 2] + 1
            mapping[i] = mapping[int((i - 1))] + " " + str(i)

    return Num_Op_List[n - 1], mapping[n]
n = int(input())
l1, m1 = Prim_Calc(n)
print(l1)
print(m1)
