my_list = [12, 10, 9, 6, 6, 3, 2, 1, 1]
num = int(input("Введите новый элемент рейтинга:"))
for n, el in enumerate(my_list):
    if  num > el:
        my_list.insert(n, num)
        break
if num <= el:
        my_list.append(num)
print(my_list)



