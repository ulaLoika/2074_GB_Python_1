def convert_name_extract(list_in):
    for element in range(len(list_in)):
        list_in[element] = list_in[element].split()
        list_in[element] = f'Привет, {list_in[element][-1].capitalize()}'

    return list_in


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)