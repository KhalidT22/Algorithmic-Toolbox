
import math
def BinarySearch(arr1, value):
    left = 0
    right = len(arr1)-1
    index = -1
    while right >= left:
        middle = math.floor((left + right) / 2)
        if arr1[middle] == value:
            index = middle
            right = middle -1
        elif arr1[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return index

def majority_element(n,arr1):
    limit = math.floor(n/2)
    arr1 = sorted(arr1, key=lambda x: x, reverse=False)
    index = 0
    output =0

    while index <= math.ceil(n/2)-1:
        check = min(index + limit,n-1)

        if arr1[index] == arr1[check]:
            output = 1
            return output
        else:
            index = BinarySearch(arr1, arr1[check])
    return output

import  sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr1 = data[1:n+1]
print(majority_element(n,arr1))