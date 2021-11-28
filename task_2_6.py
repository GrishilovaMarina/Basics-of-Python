class Road:
    weight_on_one = 0.025
    thickness = 5
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def weight(self):
         return self._length * self._width * Road.weight_on_one * Road.thickness

my_road = Road(20, 5000)
print(my_road.weight(), "тонн")
