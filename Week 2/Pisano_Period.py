def pisano(m):
    prev_elm = 0
    cur_elm = 1
    for i in range(0,m*m+1):
        next_elm = (prev_elm + cur_elm) % m
        prev_elm = cur_elm
        cur_elm = next_elm
        if(cur_elm == 1) & (prev_elm == 0):
            return i+1

print(pisano(3))