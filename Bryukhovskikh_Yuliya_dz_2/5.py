# импортируем функцию random из модуля randint
from random import randint


def rub_cop(lst):
    """функция приводит цены к единому формату * руб. ** коп."""
    for i in lst[:-1]:
        rub = int(i*100//100)
        cop = str(int(i*100%100))
        print(f"{rub} руб. {cop.zfill(2)} коп.", end=", ")
    rub = int(lst[-1] * 100 // 100)
    cop = str(int(lst[-1] * 100 % 100))
    print(f"{rub} руб. {cop.zfill(2)} коп.")


prices = list()
# генерируем случайный список из 20 позиций
for i in range(20):
    prices.append(randint(1, 10000)/100)
# выводим на печать
rub_cop(prices)
id1 = id(prices)
# сортируем список по возрастанию
prices.sort()
# выводим на печать
rub_cop(prices)
id2 = id(prices)
# сравниваем объекты
print(f"{id1} - id объекта до сортировки, {id2} - id объекта после сортировки")
# сортируем список по убыванию
prices2 = sorted(prices, reverse=True)
# выводим на печать про возрастанию 5 самых дорогих
rub_cop(sorted(prices2[:5]))