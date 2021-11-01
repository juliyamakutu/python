import sys
from utils import currency_rates

# если нет параметров командной строки или их больше одного - то выводим usage
if len(sys.argv) != 2:
    print(f'Usage: python {sys.argv[0]} <currency>')
    exit(1)

# получаем курс и дату
value, date = currency_rates(sys.argv[1])
# если такая валюта не найдена - напишем об этом
if value is None:
    print(f'Валюта {sys.argv[1]} не найдена')
    exit(1)

# выводим курс и дату
print(value, date, sep=', ')