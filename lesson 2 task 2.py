l = input('введите список значений:')
my_list = l.split()
print(my_list)
for i in range(0, len(my_list) - 1, 2):
    temp = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = temp

print(my_list)


