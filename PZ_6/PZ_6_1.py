# Дан список размера N и целые числа K и L (1 < K <= L <= N).
# Найти среднее арифметическое всех элементов списка
# кроме элементов с номерами от К до L.

try:  # Обработчик исключений
    N = int(input('Введите размер списка: '))  # Ввод размера списка
    print('Введите два целых числа K и L, которые (1 < K <= L <= N)')
    K = int(input('Значение К: '))  # Ввод К
    L = int(input('Значение L: '))  # Ввод L
    if (K > 1) and (L >= K) and (N >= L):  # Провепка условия (1 < K <= L <= N)
        a = []  # Вводим пустой список для записи чисел
        b = N  # Счетчик для цикла
        while b != 0:
            a.append(float(input('Введите число: ')))  # Заполняем список значениями в кол-ве N
            b -= 1
        x = a[:K]  # Делаем срез списка до элемента с номером К
        z = a[L + 1:]  # Срез списка после элемента с номером L
        x.extend(z)  # Увеличиваем список x значениями из списка z
        print(sum(x) / len(x))  # Находим среднее арифметическое
    else:
        print('Введенные числа не подходят')
except ValueError:
    print('Неверно введенные данные')