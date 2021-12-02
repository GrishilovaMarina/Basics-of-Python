from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, title, param):
        self.title = title
        self.param = param
    @abstractmethod
    def calc(self):
        pass
    def __str__(self):
        return f'{self.title}, {self.param}'
class Coat(Clothes):
    @property
    def calc(self):
        return round(self.param / 6.5 + 0.5, 2)
class Suit(Clothes):
    @property
    def calc(self):
        return round(2 * self.param + 0.3, 2)

print(Coat('Пальто женское', 46))
a = Coat('Пальто женское', 46).calc
print(a)
print(Suit('Костюм мужской', 1.80))
b = Suit('Костюм мужской', 1.80).calc
print(b)

print(f'Общий расход ткани: {a + b}')