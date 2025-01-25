def different_summands(x):
    list = []
    count = 1

    while  x>0:


        list.append(count)

        x -= count

        count += 1
        if x == 0:
            return list
        else:
            if x  >= count:

                continue
            else:
                x += count-1
                list.pop()

    return list

n = int(input())
list1 = different_summands(n)

print(len(list1))
print(" ".join(map(str,list1)))