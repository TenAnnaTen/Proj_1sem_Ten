# дано число А (>1)
# вывести наибольшее из целых чисел К
# Для которых сумма 1 + 1/2 + ... + 1/К будет меньше А и эту сумму

try:  # обработчик исключений
    A = float(input('Введите число, большее 1: '))
    if A > 1:  # проверка условия, что A > 1
        b = 1
        K = 2
        while b <= A:
            b += 1 / K
            K += 1
        b -= 1 / K  # выделяем прошлую итерацию
        K -= 2  # выделяем последнее подходящее значение К
        print(f'K = {K}. Сумма: {b}')
    else:
        print('Число не больше 1')
except:
    print('Неверно введённые данные')