def my_func(x, y):
    while y >= 0:
        print("Неверно введено число:")
        y = int(input('Введите целое отрицательное число:'))
        continue
    if y < 0:
        y = - y
        result = 1 / (x ** y)
        print(result)

x = int(input('Введите действительное положительное число:'))
y = int(input('Введите целое отрицательное число:'))
my_func(x, y)



def my_func(x, y):
    while y >= 0:
        print("Неверно введено число:")
        y = int(input('Введите целое отрицательное число:'))
        continue
    if y < 0:
        y = - y
        res_1 = x
        for i in range(1, y):
            res_1 = res_1 * x
        result = 1 / res_1
        print(result)
x = int(input('Введите действительное положительное число:'))
y = int(input('Введите целое отрицательное число:'))
my_func(x, y)
