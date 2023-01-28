# Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц.
import random
from functools import reduce

# генерируем случайный список оценок от 2 до 5
ocenki = [random.randint(2, 5) for i in range(random.randint(2, 10))]
# выводим текущий список оценок
print(f'Текущие оценки: {ocenki}')
# считаем сумму всех оценок
itog = reduce(lambda x, y: x + y, ocenki)
# используя генератор списка, выделяем оценки 2, 3, 4, 5 в отдельные списки
dva = [i for i in ocenki if i == 2]
tri = [i for i in ocenki if i == 3]
chet = [i for i in ocenki if i == 4]
pyat = [i for i in ocenki if i == 5]
# выводим количество каждой оценки
print(
    f'Количество "2": {len(dva)}\nКоличество "3": {len(tri)}\nКоличество "4": {len(chet)}\nКоличество "5": {len(pyat)}')
# выводим итоговую оценку за месяц (среднее арифметическое)
print(f'Итоговая оценка за месяц: {round(itog/len(ocenki))}')

