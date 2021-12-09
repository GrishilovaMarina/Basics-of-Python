class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'z = ({self.a} + {self.b}i)'

    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        return f'z_sum = ({res_a} + {res_b}i)'

    def __mul__(self, other):
        res_a = self.a * other.a - self.b * other.b
        res_b = self.a * other.b + self.b * other.a
        return f'z_mul = ({res_a} + {res_b}i)'


z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(-1, 1)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
