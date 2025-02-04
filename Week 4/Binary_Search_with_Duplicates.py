
import math


def binary_search(n,m,arr1,arr2):
    arr3 = ""

    for i in range(0,m):
        value = arr2[i]
        arr3 += str(BinarySearch(arr1, value))+" "
    return arr3

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

import  sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr1 = data[1:n+1]
m = data[n+1]
arr2 = data[n+2:]
print(binary_search(n,m,arr1,arr2))
