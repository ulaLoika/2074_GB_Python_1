result = [12, 44, 4, 10, 78, 123]

'''если важна не память, а скорость применяем лист компрехеншн'''
def get_numbers(src):
    return [src[i + 1] for i in range(len(src)-1) if src[i] < src[i+1]]

'''если важна память, а не скорость, то применяем генераторы'''
def get_numbers_gen(src):
    for i in range(len(src) - 1):
        if src[i] < src[i+1]:
            yield src[i + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
gen = get_numbers_gen(src)
print (type(gen))

for el in gen:
    print (el)

