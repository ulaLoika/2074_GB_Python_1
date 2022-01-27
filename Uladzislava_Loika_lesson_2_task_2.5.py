import random
from random import uniform


def transfer_list_in_str(list_in):
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    str_out = ''
    for el in range(len(list_in)):
        element = str(list_in[el])
        num_before_dot = int(element[:2])
        num_after_dot = element[3:]
        if num_after_dot == '0':
            num_after_dot += '0'
        if len(num_after_dot) < 2:
            num_after_dot = str(int(num_after_dot * 10))
        if el != len(list_in) - 1:
            str_out += f'{num_before_dot} руб {num_after_dot} коп, '
        else:
            str_out += f'{num_before_dot} руб {num_after_dot} коп'

    return str_out


my_list = [round(random.uniform(10, 100), 2) for _ in range(1, 10)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
id_result_1 = id(my_list)
id_result_2 = id(result_2)
if id_result_2 == id_result_1:
    print('Номер ID прежний.')
else:
    print ('Номер ID изменился.')


def sort_price_adv(list_in):
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_in.sort(reverse=True)
    list_out = list_in
    return list_out


result_3 = sort_price_adv(my_list)
print(f'Список по убыванию: {result_3}')


def check_five_max_elements(list_in):
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    for i in range(5):
        list_out.append(list_in[i])
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'Пять максимальных значений списка: {result_4}')