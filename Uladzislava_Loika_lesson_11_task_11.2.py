class CustomZeroException(Exception):
    def __init__(self, mes):
        self.mes = mes


def zero_division_func(x, y):
    try:
        if y == 0:
            raise CustomZeroException('Второе число не может быть нулем!')
        else:
            return f'Ответ: {int(x / y)}'
    except CustomZeroException as message:
        return message


x = int(input('X: '))
y = int(input('Y: '))
print(zero_division_func(x, y))
