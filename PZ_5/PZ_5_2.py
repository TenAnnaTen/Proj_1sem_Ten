# Описать функцию Mean(X, Y, AMean, GMean)
# вычисляющую среднее арифметическое AMean=(X+Y)/2 и среднее геометрическое GMean=X/Y двух положительных чисел X и Y.
# X и Y - входные, AMean и  GMean - выходные параметры вещественного типа.
# Найти среднее арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны A B C D.

def Mean(X, Y):
    AMean = (X + Y) / 2
    GMean = Y / X
    print(f'Cреднее арифметическое: {AMean}')
    print(f'Cреднее геометрическое: {GMean}')


try:
    A = float(input('Введите значения A, B, C, D. Значение А (> 0): '))
    B = float(input('Значение B: '))
    C = float(input('Значение C: '))
    D = float(input('Значение D: '))
    print('Для A и B')
    Mean(A, B)
    print('Для A и C')
    Mean(A, C)
    print('Для A и D')
    Mean(A, D)
except TypeError:
    print('Введите числа')
except ZeroDivisionError:
    print('Введите А > 0')
