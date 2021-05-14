# задание 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Виктор'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generator(tutors, klasses):
    a = zip(tutors, klasses)
    if len(tutors) > len(klasses):
        while len(tutors) != len(klasses):
            klasses.append(None)
    for i in a:
        yield i


pair = generator(tutors, klasses)
print(type(pair))

# for i in pair:
#     print(i)

while True:  # до полного истощения
    print(next(pair))
