import pprint

'''задание 6.1 и 6.2 в одном файле'''
def parsing_func (element):
    list_str = element.split(' ')
    return list_str[0], list_str[5][1:], list_str[6]

parsed_data = []
with open('nginx_logs.txt', 'r', encoding = 'utf-8') as f:
    for string in f:
        parsed_data.append(parsing_func(string))
    print(parsed_data)
    temp = []
    counter = 0
    for el in parsed_data:
        temp.append(el[0])
    for i in temp:
        element_frequency = temp.count(i)
        if (element_frequency > counter):
            counter = element_frequency
            num = i
    print ()
    print (f'IP спамера: {num}')


