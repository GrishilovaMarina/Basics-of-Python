class DivError(Exception):
    def __init__(self, text):
        self.text = text
try:
    dividend = int(input('Введите делимое:  '))
    divider = int(input('Ведите делитель:  '))

    if divider == 0:
       raise DivError('Деление на ноль недопустимо')
    else:
        print(dividend / divider)
except DivError as err:
    print(err)
