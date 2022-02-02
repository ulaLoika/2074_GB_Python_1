from random import choice


def get_jokes(count):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_out = []
    common_list = [nouns, adverbs, adjectives]
    for el in range(count):
        jokes_list = list(map(choice, common_list))
        list_out.append(' '.join(jokes_list))

    return list_out


print(get_jokes(3))