import json
with open('my_text_7.txt', 'r+', encoding='utf-8') as file_obj:
    content = file_obj.readlines()
    my_dict_1 = {}
    my_dict_2 = {}
    sum_profit = 0
    number = 0
    for el in content:
        param = el.split()
        my_dict_1[param[0]] = (int(param[2]) - int(param[3]))
        if int(param[3]) < int(param[2]):
            sum_profit += (int(param[2]) - int(param[3]))
            number += 1
    my_dict_2['average_profit'] = float(sum_profit / number)
    my_list = [my_dict_1, my_dict_2]
    print(my_list)

with open('my_file.json', 'w') as file_obj_2:
    json.dump(my_list, file_obj_2)
