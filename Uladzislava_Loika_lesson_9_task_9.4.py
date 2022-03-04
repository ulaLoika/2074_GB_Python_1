from sys import stdout

class Car:
    is_police = False
    max_speed = 0
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        self.speed = self.speed + 15
        stdout.write(f'Машина {self.name} повысила скорость на 15: {self.speed}.\n')

    def stop(self):
        stdout.write(f'{self.name} остановилась. Скорость равна: {self.speed - self.speed}.\n')

    def turn(self, direction):
        if direction in ('направо', 'налево', 'прямо', 'назад'):
            stdout.write(f'{self.name} движется {direction}.\n')
        else:
            raise ValueError ('Введите направление движения!')

    def show_speed(self):
        if self.is_police:
            stdout.write(f'{self.name} текущая скорость {self.speed} км/час.\n'
                         f'Вруби мигалку и забудь про скорость!\n')
        else:
            if self.speed > self.max_speed:
                stdout.write(f'Alarm!!! Speed!!!: {self.speed}\n')
            else:
                stdout.write(f'{self.name} текущая скорость {self.speed} км/час.\n')


class TownCar(Car):
    max_speed = 60

class WorkCar(Car):
    max_speed = 40

class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police = True


if __name__ == '__main__':
    town_car = TownCar(41, 'red', 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, 'blue', 'Ferrari')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()
    town_car.show_speed()
    work_car.show_speed()
    town_car.stop()
    police_car.show_speed()
    sport_car.turn('назад')


