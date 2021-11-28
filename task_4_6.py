class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return 'Машина поехала'
    def stop(self):
        return 'Машина остановилась'
    def turn(self):
        return 'Машина повернула...'
    def show_speed(self):
        return self.speed
class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        if self.speed > 60:
            print('Превышение допустимой скорости')
        return self.speed
class SportCar(Car):
    def __init__(self, speed, color, name):
       super().__init__(speed, color, name, False)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        if self.speed > 40:
            print('Превышение допустимой скорости')
        return self.speed
class PoliceCar(Car):
    def __init__(self, speed, color, name):
       super().__init__(speed, color, name, True)

print(TownCar(70, 'red', 'Mazda').show_speed())
print(SportCar(120, 'black', 'Porsche').go())
print(WorkCar(50, 'green', 'GAZ').stop())
print(PoliceCar(90, 'white', 'BMW').turn())

