from time import sleep
from sys import exit

class TrafficLight:
    __color = {'red': 4, 'yellow': 2, 'green': 3}
    colors_list = ['red', 'yellow', 'green']

    def running(self):
        for key, value in self.__color.items():
            print (f'{key} {value} сек')
            sleep(value)

    """задаем первый цвет светофора и проверям,
    соответсвует ли онправильному первому цвету из словаря цветов светофора."""
    def __init__(self, initial_color = 'red'):
        self.initial_color = initial_color
        if not initial_color == self.colors_list[0]:
            exit('The first color of Trafficlight should be "red"!')

if __name__ == '__main__':
    traf_light = TrafficLight('red')
    traf_light.running()

