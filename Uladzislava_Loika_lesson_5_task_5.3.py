tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Михаил', 'Яна', 'Максим', 'Андрей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors, klasses):
    for el in range (len(tutors)):
        yield (tutors[el], klasses[el]) if el < len(klasses) else tutors[el], None


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration