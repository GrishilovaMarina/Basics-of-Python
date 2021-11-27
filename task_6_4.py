from itertools import count, cycle
n = int(input())
for el in count(3):
    if el > n:
        break
    else:
        print(el)

l = input()
ind = 0
for el in cycle(l):
    if ind >= n:
        break
    else:
        print(el)
        ind = ind + 1


