with open('my_text_6.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.readlines()
    my_dict = {}
    for el in content:
        param = el.split()
        sum = 0
        for i in range(1, len(param)):
            if param[i] != '-':
                sum = sum + int(param[i].split('(')[0])
        my_dict[param[0]] = sum
    print(my_dict)
