
def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i
#указываем диапазон
if __name__ == "__main__":
    a_gen = odd_num(15)
#тип переменных
    print("a_gen type", type(a_gen))
#вызов элементов генератора
    for elem in a_gen:
        print(elem)