class MyError(Exception):
    def __init__(self, text):
        self.text = text
my_list = []
while True:
    try:
        arg = input('Введите число или "stop":  ')
        if arg == 'stop':
            print(my_list)
            break
        if not arg.isdigit():
            raise MyError('Вы ввели не число')
        else:
            my_list.append(arg)
    except MyError as err:
        print(err)
