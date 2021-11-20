with open('my_text_1.txt', 'x') as file_obj:
    while True:
        content = input()
        if content == '':
            print('Ввод данных окончен')
            file_obj.close()
            break
        else:
            file_obj.write(content + '\n')


