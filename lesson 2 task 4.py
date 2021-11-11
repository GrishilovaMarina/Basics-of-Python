str = input('Введите строку из нескольких слов:')
my_list = str.split()
for el in enumerate(my_list):
     print(f"{el[0]+1} . {el[1][:10]}")

