number = int(input("Введите исходное количество секунд:"))
hour = number// 3600
minute = number % 3600 // 60
second = (number % 3600) % 60
print(f"Время {hour:02}:{minute:02}:{second:02}")


