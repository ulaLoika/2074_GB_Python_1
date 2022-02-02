def num_translate(key: str) -> str:
    eng_ru_dictionary = {'one': 'один', 'two': "два", 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                         'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    if key.lower() in eng_ru_dictionary.keys():
        if key.islower():
            return eng_ru_dictionary.get(key.lower()).lower()
        return eng_ru_dictionary.get(key.lower()).title()


print(num_translate('Two'))
print(num_translate('one'))
print (num_translate('bla'))
print(num_translate('Three'))
