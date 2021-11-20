with open('my_text_3.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.readlines()
    print('Список сотрудников, чей оклад менее 20000:')
    sum_income = 0
    for el in content:
        words = el.split()
        sum_income += float(words[2])
        if float(words[2]) < 20000:
            print(el)
    print('Средняя величина дохода сотрудников равна:', float(sum_income / len(content)))

