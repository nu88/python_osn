
price = [57.9, 30.51, 20.87, 40.35, 97, 88.9, 37.9, 58.44, 44.39, 68]
for index in range(len(price)):
    price1 = sorted(price, reverse=True)
    print(f'{"%d" % price1[index]} руб', f'{int(price1[index]%1*100)} коп')#f'{"%d" % round(price[index]%1, 1)*10} коп')

print(type(price1) == type(price))

for index in range(len(price)):
    price2 = sorted(price, reverse=False)
    print(f'{"%d" % price2[index]} руб', f'{int(price2[index]%1*100)} коп')#f'{"%d" % round(price[index]%1, 1)*10} коп')

result = price1[:5]
print('Пятерка самых дорогих товаров', result)
