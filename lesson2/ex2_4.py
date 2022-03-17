spisok = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = [item.split()[-1] for item in spisok]
for name in names:
    print (f'Привет, {name.title()}!')