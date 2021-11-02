from typing import Generator, List, Tuple


def my_map(tutors: List[str], klasses: List[str]) -> Generator[Tuple[str], None, None]:
    for i in range(len(tutors)):
        tutor = tutors[i]
        if i < len(klasses):
            klass = klasses[i]
        else:
            klass = None
        yield (tutor, klass)


# списки для проверки
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# проверяем генератор
print('первая проверка')
a = my_map(tutors, klasses)
for i in a:
    print(i)

# второй набор списков для проверки
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Ольга', 'Наталья']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# проверяем генератор
print('вторая проверка')
a = my_map(tutors, klasses)
for i in a:
    print(i)