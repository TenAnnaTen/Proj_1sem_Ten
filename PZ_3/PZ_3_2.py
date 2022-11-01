# Даны два числа. Вывести большее из них.
while True:
    try:  # обработчик исключений
        chislo_1, chislo_2 = float(input('Введите два числа. Первое: ')), float(input('Второе: '))
        if chislo_1 > chislo_2:
            print(f'Первое число: {chislo_1}. Второе: {chislo_2}. Большее их них: {chislo_1}')
            break
        else:
            print(f'Первое число: {chislo_1}. Второе: {chislo_2}. Большее их них: {chislo_2}')
            break

    except:  # исключения
        print('Неравильно введенные данные, попробуйте ещё раз')
        continue