a = int(input("Введите начальный результат пробежки в первый день:"))
print(f"{a} км")
b = int(input("Введите желаемый результат пробежки:"))
print(f"{b} км")
day = 1
while a < b:
    a = a * 1.1
    day += 1
print(f"При ежедневном увеличении результата на 10% желаемый результат пробежки будет достигнут на {day} день ")

