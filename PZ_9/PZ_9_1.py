# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

def maxi(m, n):
    for i in range(0, len(n)):
        if m < int(n[i]):
            m = int(n[i])
    print(f'Максимальная продажа: {m}')


a = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'.split()
b = {}
c = {}
b1 = []
c1 = []
for i in range(1, 6):
    b1.append(a[i])
for j in range(7, 12):
    c1.append(a[j])
b[a[0]] = b1
c[a[6]] = c1
print(b, c)
maxi(0, b1)
maxi(0, c1)
