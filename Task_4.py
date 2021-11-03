number = int(input("Введите целое положительное число:"))
n_max = 0
while number > 10:
    n = number % 10
    if n > n_max:
        n_max = n

    number = number // 10
print(f"Самая большая цифра в числе: {n_max}")


