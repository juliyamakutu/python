from typing import Generator


def odd_nums(n: int) -> Generator[int, None, None]:
    return (i for i in range(1, n+1, 2))


# проверяем работу функции

# получаем генератор
a = odd_nums(15)

# проходим циклом по генератору
for i in a:
    print(i, end=', ')
# переводим строку
print('')