# #Вариант 1
# def parse_log(pth_file):
#     if pth_file:
#         with open(pth_file, "r", encoding="utf-8") as file:
#             for line in file:
#                 remote_addr = line.split(" - - ")[0]
#                 request_type_rem = line.split('"')[1]
#         yield (remote_addr, request_type_rem)
#
#         #remote_addr = i[:14]
#         # request_type = i[49:52]
#         # requested_resource = i[53:73]
# #pth_file = open('nginx_logs.txt', 'r')
# a = parse_log("./nginx_logs.txt")
# for e in a:
#     print(e)

#Вариант 2 срезы

# def parse_log(pth_file):
#     if pth_file:
#         with open(pth_file, "r", encoding="utf-8") as file:
#             for line in file:
#                 remote_addr = line[:14]
#                 request_type = line[49:52]
#                 requested_resource = line[53:73]
#         yield (remote_addr, request_type, requested_resource)
# a = parse_log("./nginx_logs.txt")
# for e in a:
#      print(e)

# Вариант 3 регулярные выражения

# import re
# regex = (r'\d{3}\.\d{3}\.\d{3}\.\d{3}')
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     print(re.findall(regex, f.read()))

# Вариант 4 после разбора ДЗ

# with open ('nginx_logs.txt', "r", encoding="utf-8") as file:
#     requests_list = []
#     for line in file:
#         #находим первое вхождение пробела при помощи среза чтобы найти IP
#         remore_addr = line[:line.find(' ')]
#         # находим ковычки, +4 это значит отступы
#         requests_type = line[line.find('"') + 1:line.find('"') + 4]
#         requested_resource = line[line.find('/d'):line.find('HTTP') - 1]
#         tuple_requests = (remore_addr, requests_type, requested_resource)
#         #формируем кортеж и добавляем в список
#         requests_list.append(tuple_requests)
#         print(tuple_requests)

# Вариант 5 после разбора ДЗ

# data_list = []
#
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         var = line.strip().split()
#         data_list.append((var[0], var[5], var[6]))
# print(data_list[:6])