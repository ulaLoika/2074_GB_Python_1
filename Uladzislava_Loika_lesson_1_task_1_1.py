def convert_time(duration: int):
    return f" {duration // 86400 % 361} дн {duration // 3600 % 24} час" \
        f" {duration // 60 % 60} мин {duration % 60} сек"


duration = [400153, 10000, 5000, 76000]
for element in duration:
    result = convert_time(element)
    print(result)
