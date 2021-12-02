class Cell:
    def __init__(self, param):
        self.param = param
    def __str__(self):
        return f'{self.param}'
    def __add__(self, other):
        return self.param + other.param
    def __sub__(self, other):
        if self.param > other.param:
            return self.param - other.param
        else:
            return f'Разность количества ячеек меньше нуля'
    def __mul__(self, other):
        return self.param * other.param
    def __truediv__(self, other):
        return round(self.param / other.param)
    def make_order(self, number):
        row = ''
        for i in range(self.param // number):
            row += ('*' * number + '\n')
        row = row + '*' * (self.param % number)
        return {row}

a = Cell(16)
b = Cell(7)
c = Cell(10)
print('результат сложения: ', a + b)
print('результат вычитания: ', b - c)
print('результат вычитания: ', a - c)
print('результат умножения: ', b * c)
print('результат деления: ', a / b)
print(a.make_order(5))