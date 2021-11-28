class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручкой'
class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандашом'
class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркером'

print(Pen('ручка').draw())
print(Pencil('карандаш').draw())
print(Handle('маркер').draw())

