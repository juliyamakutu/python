from typing import Optional


# создаём словарь для перевода как константу
DICT = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "seven": "семь",
    "six": "шесть",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}


def num_translate(word: str) -> Optional[str]:
    # получаем перевод из словаря, если такого ключа нет get вернёт None
    return DICT.get(word)


# Проверяем работу функции на тестовых данных
print('Перевод "one":', num_translate('one'))
print('Перевод "five":', num_translate('five'))
print('Перевод "seven:"', num_translate('seven'))
print('Перевод "eleven":', num_translate('eleven'))