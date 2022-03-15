class Warehouse_of_machines():
    final_warehouse = []

    def __init__(self):
        self.warehouse = []
        self.one_machine = {}
        self.action = None

    def inputting_machines(self):
        try:
            name = input(f'наименование: ')
            cost = input(f'цена за ед: ')
            quantity = input(f'количество: ')
            self.action = input(f'количество операций машины: ')
            one_machine_data = {'модель устройства': name, 'цена за ед': cost, 'количество': quantity}
            self.one_machine.update(one_machine_data)
            self.warehouse.append(self.one_machine)
            print(f'Текущий список -\n {self.warehouse}')
        except TypeError:
            return 'Ошибка ввода данных'

        print(f'Чтобы выйти, введите - NOT, чтобы продолжить - любой символ на клавиатуре.')
        NOT = input(' ')
        if NOT == 'NOT':
            Warehouse_of_machines.final_warehouse.append(self.warehouse)
            print (f'На складе находятся следующая аргтехника: {Warehouse_of_machines.final_warehouse}')
        else:
            return Warehouse_of_machines.inputting_machines


class Printer(Warehouse_of_machines):
    def action(self):
        return f'Количество копий принтера: {self.action}'


class Scanner(Warehouse_of_machines):
    def action(self):
        return f'Количество копий сканера:{self.action}'


class Copier(Warehouse_of_machines):
    def action(self):
        return f'Количество копий ксерокса: {self.action}'


printer_obj = Printer()
scaner_obj = Scanner()
copier_obj = Copier()

printer_obj.inputting_machines()
scaner_obj.inputting_machines()
copier_obj.inputting_machines()
print()
print()
print('END')