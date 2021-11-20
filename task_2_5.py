with open('my_text_2.txt') as file_obj:
    content = file_obj.readlines()
    print(f"{'Всего строк в файле:'} {len(content)}")
    n = 0
    for i in range(0, len(content)):
        words = content[i].split()
        n += 1
        print(n, '.', 'количество слов в строке:', len(words))

