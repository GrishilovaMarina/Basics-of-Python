import time

class TrafficLight:
    def __init__(self, __color):
        self.__color = __color
    def running(self):
        for key, value in self.__color.items():
            print(key)
            time.sleep(value)
TrafficLight({'Red': 7, 'Yellow': 2, 'Green': 5}).running()

