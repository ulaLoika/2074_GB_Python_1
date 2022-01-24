#a)
def sum_list_1(dataset: list):
    total_sum = 0
    for i in my_list:
        didgits_sum = 0
        for j in list(str(i)):
            didgits_sum += int(j)
        if didgits_sum % 7 == 0:
            total_sum += i
    return f'сумма квадратов нечетных чисел, сумма чисел которых кратна 7: {total_sum}'

#b)
def sum_list_2(dataset: list):
    total_sum = 0
    new_list = []
    for i in range(len(my_list)):
        el = my_list[i] + 17
        new_list.append(el)
    for element in new_list:
        didgits_sum = 0
        for j in list(str(element)):
            didgits_sum += int(j)
        if didgits_sum % 7 == 0:
            total_sum += element
    return f'сумма квадратов нечетных чисел + 17, сумма чисел которых кратна 7: {total_sum}'


my_list = []
for i in range (1,100,2):
    my_list.append(i**3)

result_1 = sum_list_1(my_list)
result_2 = sum_list_2(my_list)
print(result_1)
print(result_2)
