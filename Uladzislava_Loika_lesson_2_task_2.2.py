def convert_list_in_str(list_in):
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    i = 0
    plus_or_minus = ''

    while i < len(list_in):
        if list_in[i][0] in '+-':
            plus_or_minus = list_in[i][0]
        if list_in[i].isdigit() or (plus_or_minus and list_in[i][1:].isdigit()):
            if plus_or_minus:
                list_in[i] = plus_or_minus + list_in[i][1:].zfill(2)
            else:
                list_in[i] = list_in[i].zfill(2)

            list_in.insert(i, '"')
            list_in.insert(i + 2, '"')
            i += 2
        i += 1

    str_out = ' '.join(list_in)

    return(str_out)


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

