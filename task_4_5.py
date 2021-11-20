with open('my_text_4.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.readlines()
    my_dict = {'Один': 'One', 'Два': 'Two', 'Три': 'Three', 'Четыре': 'Four'}
    with open('my_text_4_1.txt', 'w', encoding='utf-8') as file_obj_2:
        for el in content:
            def get_key(my_dict, value):
                for k, v in my_dict.items():
                    if v == value:
                        return k
            new_content = file_obj_2.write((get_key(my_dict, el.split()[0])) + ' - ' + el.split()[2] + '\n')

