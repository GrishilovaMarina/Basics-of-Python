class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return(self.name + ' ' + self.surname)
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']
my_doc = Position('Иван', 'Иванов', 'директор', 1000, 200)
print(my_doc.get_full_name())
print('доход сотрудника с учетом премии:', my_doc.get_total_income())

