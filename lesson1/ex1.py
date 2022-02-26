duration = input('Введите значение в секундах')
time = int(duration)
day = time//86400
days = ['день', 'дня', 'дней']
if day % 10 == 1 and day % 100 != 11:
    p = 0
elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
    p = 1
else:
    p = 2
if time <= 60:
    print(time, 'сек')
elif time <= 3600:
    print(time//60, 'мин', time % 60, 'сек')
elif time <= 86400:
    print(time//3600, 'час', time % 3600//60, 'мин', time % 3600 % 60, 'сек')
else:
    print(day, days[p], time % 84600//3600, 'чаc', time % 86400 % 3600//60, 'мин', time % 86400 % 3600 % 60, 'сек')