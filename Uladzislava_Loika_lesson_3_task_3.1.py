def num_translate(key: str) -> str:

    eng_ru_dictionary = {'one': 'один', 'two': "два", 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if key in eng_ru_dictionary:
        str_out = eng_ru_dictionary.get(key)
    else:
        str_out = eng_ru_dictionary.get(key)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("zero"))
