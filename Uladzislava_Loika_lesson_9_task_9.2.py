class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self, hight = 5, mass_m_2 = 25):
        return int(self.length * self.width * mass_m_2 * hight / 1000)


if __name__ == '__main__':
    road = Road(1000, 6)
    print (f'Для изготовления покрытия дороги нужно {road.calculate()} тонн асфальта.')
