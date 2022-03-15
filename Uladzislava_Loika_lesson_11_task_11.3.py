class WrongType(TypeError):
    mes = 'Вы ввели не число!'


class CustomizedList:
    def __init__(self):
        self.list_custom = []

    def numbers(self):
        while True:
            try:
                number = input('\nВведите число или stop для завершения - ')
                if number == 'stop':
                    return f'\n\nВаш конечный список: {self.list_custom}'
                if not number.isdigit():
                    raise WrongType
                else:
                    self.list_custom.append(int(number))

            except WrongType as mes:
                print(WrongType.mes)



user_number = CustomizedList()
print(user_number.numbers())
