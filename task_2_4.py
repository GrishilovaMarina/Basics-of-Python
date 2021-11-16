list = [15, 22, 3, 8, 12, 5, 4, 32]
new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(new_list)