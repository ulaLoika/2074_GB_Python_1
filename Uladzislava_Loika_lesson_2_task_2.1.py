def identify_type (element):
    return type(element)

data = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for el in data:
    print (identify_type(el))

