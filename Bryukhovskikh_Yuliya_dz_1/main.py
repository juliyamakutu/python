for duration in (400153, 52698, 0, 18, 3000, 10153):
    secs = duration%60
    mins = duration//60%60
    hours = duration//60//60%24
    days = duration//60//60//24
    if days > 0:
        print(days, "дн.", hours,"ч.", mins, "мин.", secs, "сек.")
    elif hours > 0:
        print(hours, "ч.", mins, "мин.", secs, "сек.")
    elif mins > 0:
        print(mins, "мин.", secs, "сек.")
    else:
        print(secs, "сек.")