proceeds = int(input("Введите сумму выручки в рублях:"))
costs = int(input("Введите сумму издержек в рублях:"))
profit = proceeds - costs
print(f"Прибыль предприятия составляет: {profit} руб")
profitability = profit / costs * 100
print(f"Рентабельность предприятия равна {profitability} процентов")
number = int(input("Численность сотрудников предприятия:"))
person_profit = profit / number
print(f"Прибыль предприятия в расчете на одного сотрудника составляет {person_profit:.2f} руб")

