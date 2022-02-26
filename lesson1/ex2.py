cubes = [(x**3) for x in range(100) if x%2 != 0]
print('Список кубов нечетных чисел', (cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers =[]
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
#Вычисляем сумму чисел в списке
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]
#В случае если сумма чисел делится на 7
    if my_numbers_sum % 7 == 0:
        print('Cумма чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)
print('Список чисел, делящихся на 7: ',my_numbers_sum_list_even_numbers)