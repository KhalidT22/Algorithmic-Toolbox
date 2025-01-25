import sys
def car_fueling(d,m,n,stops):
    num_refill = 0
    if m > d:
        return num_refill
    elif m < stops[0]:
        return -1
    else:
        if stops[-1] != d:
            stops.append(d)

        cur_fuel = m
        cur_dis = 0
        for i in range(0, n+1 ):
            if cur_dis == d:
                break
            if cur_fuel >= stops[i] - cur_dis:
                #go

                cur_fuel = cur_fuel - (stops[i] - cur_dis)
                cur_dis = stops[i]

            elif m >= stops[i] - cur_dis:
                #refill then go
                num_refill += 1
                cur_fuel = m - (stops[i] - cur_dis)
                cur_dis = stops[i]
                
            else:
                return -1
        return num_refill

data = list(map(int, sys.stdin.read().split()))

d = data[0]
m = data[1]
n = data[2]
stops = data[3:]
print(car_fueling(d,m,n,stops))