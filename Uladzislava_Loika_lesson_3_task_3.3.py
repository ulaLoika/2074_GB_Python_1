def thesaurus(*args):
    dict_out = {}
    no_dubbles = set(args)
    for name in no_dubbles:
        key = name[0]
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    sorted_dict_out = sorted(dict_out.items())
    return sorted_dict_out

print(thesaurus("Мария", "Петр", "Илья", "Иван", "Алеша", "Яша", "Анечка"))