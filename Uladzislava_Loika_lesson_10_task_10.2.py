from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = float(size)

    @abstractmethod
    def calculate(self):
        pass

    def __str__(self):
        return f'{self.size}'


class Coat(Clothes):
    @property
    def calculate(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def calculate(self):
        return round(self.size * 2 + 0.3, 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    print (coat.calculate)
    print (costume.calculate)