for i in range(1, 101):
    if (not i >= 12 or not i <= 14) and (i % 10 == 2 or i % 10 == 3 or i % 10 == 4 ):
        print (f'{i} процента')
    elif i % 10 == 1 and i !=11:
        print(f'{i} процент')
else:
    print (f'{i} процентов')