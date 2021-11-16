list = [2, 2, 8, 15, 2, 36, 8, 16, 33, 25, 15]
new_list = [i for i in list if list.count(i) == 1]
print(new_list)