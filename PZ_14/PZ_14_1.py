# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.

import re

a = []  # Пустой список для записи подходящих данных
p = re.compile(r'Частоупотребимые маски\n')  # РВ для поиска нужного раздела
p1 = re.compile(r'^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\n$')  # РВ для поиска и записи нужных строк
p2 = re.compile(r'^[0-9]*\.[0-9]*\.[0-9]*\.0*$')  # РВ для распределения строк по файлам

with open('f1.txt', 'r', encoding='UTF-8') as f1:  # Открываю файл для чтения
    text = f1.readlines()  # Считываю построчно в перемнную
    for i in text:  # Перебираю содержимое
        if re.fullmatch(p, i):  # Нахожу нужный раздел
            t = text.index(i)  # Записываю в перемнную индекс строки нужного раздела
            for j in range(t, len(text)):  # Перебираю строки найденного раздела
                if re.fullmatch(p1, text[j]):  # Поиск необходимых для записи строк в нужном разделе
                    a.append(re.sub('\n', '', text[j]))  # Добавляю элементы с спиоск, убирая \n

a2 = [i for i in a if
      re.fullmatch(p2, i)]  # создаю список, в который входят элементы с нулевым четвертым октетом

a3 = [i for i in a if i not in a2]  # создаю список с остальными элементами

with open('f2.txt', 'w', encoding='UTF-8') as f2:  # создаю файл
    f2.write('\n'.join(a2))  # вношу в него строку, сформированную из списка
    f2.write(f'\nКоличество строк: {len(a2)}')  # вношу количество строк

with open('f3.txt', 'w', encoding='UTF-8') as f3:  # создаю файл
    f3.write('\n'.join(a3))  # вношу в него строку, сформированную из списка
    f3.write(f'\nКоличество строк: {len(a3)}')  # вношу количество строк