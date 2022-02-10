def odd_nums(number):
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    return (num for num in range(1, n+1, 2))


n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)