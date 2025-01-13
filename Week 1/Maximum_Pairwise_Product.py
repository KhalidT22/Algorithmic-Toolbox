n = int(input())
arr = input()   # takes the whole line of n numbers
l = list(map(int,arr.split(' '))) #
def max_pairwise_product(l):
    max_1 = 0
    max_2 = 0
    for i in range(0,len(l)):
        if l[i] > max_1:
            max_2 = max_1
            max_1 = l[i]


        elif l[i] > max_2:
            max_2 = l[i]
    print(max_1 * max_2)
max_pairwise_product(l)
