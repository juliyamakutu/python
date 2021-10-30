def thesaurus(*args):
    result = {}
    # пройтись по списку args
    for name in args:
        # найти первую букву имени
        l = name[0]
        # если ключа нет, то создаём список
        if result.get(l) is None:
            result[l] = []
        # добавляем имя в список
        result[l].append(name)
    # соритруем словарь по алфавиту
    result = dict(sorted(result.items(), key=lambda x: x[0]))
    # возвращаем словарь
    return result


# Проверяем работу функции на тестовых данных
print(thesaurus("Иван", "Мария", "Пётрух", "Илья"))
print(thesaurus("Юлия", "Сергей", "Юлёна", "Вадим", "Андрей"))
print(thesaurus("Олька", "Ян", "Димон"))