with open('my_text_5.txt', 'w+') as file_obj:
    file_obj.write('3 16 5 8 22 134')
    file_obj.seek(0)
    content = file_obj.read()
    print(content)
    numbers = content.split()
    sum_num = 0
    for el in numbers:
        sum_num += int(el)
    print('Сумма чисел в строке равна:', sum_num)