# список для проверки
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# пустой список для результата
result = []
# проходим в цикле по src
for i in range(len(src)-1):
    # если следующий элемент больше текущего - добавляем его в новый список
    if src[i+1] > src[i]:
        result.append(src[i+1])

# выводим результат
print(result)