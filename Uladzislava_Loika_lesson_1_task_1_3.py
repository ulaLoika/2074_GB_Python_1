def transform_string(element):
    numbers = [11, 12, 13, 14]
    if element in numbers:
        return f'{element} процентов'
    if element % 10 == 1:
        return f'{element} процент'
    if 1 < element % 10 < 5:
        return f'{element} процента'
    else:
        return f'{element} процентов'


n = 101
for i in range(1,n):
    print (transform_string(i))
