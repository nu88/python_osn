import requests
from pprint import pprint
parsed_list = []
responce = requests.get('ссылка на ресурс')
with open ('nginx_logs.txt', "r", encoding="utf-8") as file:
    f.write(responce.text)
    f.seek(0)
    for line in f:
        #находим первое вхождение пробела при помощи среза чтобы найти IP
        remore_addr = line[:line.find(' ')]
        # находим ковычки, +4 это значит отступы
        requests_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('/d'):line.find('HTTP') - 1]
        #формируем кортеж и добавляем в список
        parsed_list.append(remore_addr, requests_type, requested_resource)
        print(parsed_list[:10])
list_ip = [parsed_list[i][0] for i in range(len(parsed_list))] #вытаскиваем ip из списка
max_count_ip = list_ip.count(list_ip[0])
spamm_ip = list_ip[0]
for ip in set(list_ip) #проходим по множеству и ищем максимум обращений
    if list_ip.count(ip) > max_count_ip:
        max_count_ip, spamm_ip = list_ip.count(ip), ip

print(f'\n IP адрес спамера: {spamm_ip} \nКоличество обращений: {max_count_ip}')