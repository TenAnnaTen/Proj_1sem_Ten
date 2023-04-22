import sqlite3 as sq
from inf import inf_a_b, inf_avtors, inf_book, inf_izd, inf_raz

# with sq.connect('literature.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS avtors (
#         id_avtor INTEGER PRIMARY KEY,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL
#     )""")

# with sq.connect('literature.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS razdel (
#         id_razdel INTEGER PRIMARY KEY
#     )""")

# with sq.connect('literature.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS izdatelstvo (
#         id_izdat INTEGER PRIMARY KEY,
#         city TEXT NOT NULL
#     )""")

# with sq.connect('literature.db') as con:
#     con.execute('PRAGMA foreign_keys = ON')
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS books (
#         id_book INTEGER PRIMARY KEY,
#         nazvanie TEXT NOT NULL,
#         id_razdel INTEGER,
#         id_izdat INTEGER,
#         god_izdan INEGER NOT NULL,
#         mesto_hranen TEXT NOT NULL,
#         FOREIGN KEY (id_razdel) REFERENCES razdel(id_razdel) ON DELETE CASCADE ON UPDATE CASCADE,
#         FOREIGN KEY (id_izdat) REFERENCES izdatelstvo(id_izdat) ON DELETE CASCADE ON UPDATE CASCADE
#     )""")

# with sq.connect('literature.db') as con:
#     con.execute('PRAGMA foreign_keys = ON')
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS avtor_books (
#         id_avtora_book INTEGER PRIMARY KEY,
#         id_avtor INTEGER,
#         id_book INTEGER,
#         FOREIGN KEY (id_avtor) REFERENCES avtors(id_avtor) ON DELETE CASCADE ON UPDATE CASCADE,
#         FOREIGN KEY (id_book) REFERENCES books(id_book) ON DELETE CASCADE ON UPDATE CASCADE
#     )""")

# with sq.connect('literature.db') as con:
#      cur = con.cursor()
#      con.executemany("INSERT INTO avtors VALUES(?, ?, ?)", inf_avtors)
#      con.executemany("INSERT INTO razdel VALUES(?)", inf_raz)
#      con.executemany("INSERT INTO izdatelstvo VALUES(?, ?)", inf_izd)
#      con.executemany("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)", inf_book)
#      con.executemany("INSERT INTO avtor_books VALUES(?, ?, ?)", inf_a_b)
#      con.commit()

with sq.connect('literature.db') as con:
    cur = con.cursor()
    print("На выборку:\n")
    # Получить список всех книг, отсортированных по году издания
    res1 = con.execute("SELECT nazvanie, god_izdan FROM books ORDER BY god_izdan").fetchall()
    print(f'1:\n{res1}\n')
    # Получить список всех книг заданного автора.
    res2 = cur.execute(
        "SELECT avtors.name, books.nazvanie FROM books \
        JOIN avtor_books ON avtor_books.id_book = books.id_book \
        JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor \
        WHERE avtors.name = 'Иван'").fetchall()
    print(f'2:\n{res2}\n')
    # Получить список всех книг из заданного раздела.
    res3 = cur.execute(
      "SELECT razdel.id_razdel, books.nazvanie FROM books \
      JOIN razdel ON razdel.id_razdel = books.id_razdel \
      WHERE razdel.id_razdel = 7").fetchall()
    print(f'3:\n{res3}\n')
    # Получить список всех книг, изданных заданным издательством
    res4 = cur.execute(
        "SELECT izdatelstvo.city, izdatelstvo.id_izdat, books.nazvanie FROM books \
        JOIN izdatelstvo ON izdatelstvo.id_izdat = books.id_izdat \
        WHERE izdatelstvo.id_izdat = 3").fetchall()
    print(f'4:\n{res4}\n')
    # Получить список всех авторов в алфавитном порядке
    res5 = con.execute("SELECT * FROM avtors ORDER BY surname").fetchall()
    print(f'5:\n{res5}\n')
    # Получить список всех книг, отсортированных по названию и году издания.
    res6 = con.execute("SELECT nazvanie, god_izdan FROM books ORDER BY nazvanie, god_izdan").fetchall()
    # Фильтр изначально идёт по алфавиту,
    # по возрстанию года фильтр будет работать только если есть несколько книг с одинаковым названием
    print(f'6:\n{res6}\n')
    # Получить список всех книг заданного автора, отсортированных по году издания
    res7 = cur.execute(
        "SELECT avtors.surname, books.nazvanie, god_izdan FROM books \
        JOIN avtor_books ON avtor_books.id_book = books.id_book \
        JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor \
        WHERE avtors.surname = 'Ершов' ORDER BY god_izdan").fetchall()
    print(f'7:\n{res7}\n')
    # Получить список всех книг, опубликованных в заданном году.
    res8 = con.execute("SELECT nazvanie, god_izdan FROM books WHERE god_izdan = 2005").fetchall()
    print(f'8:\n{res8}\n')
    # Получить список всех авторов, написавших книги для заданного издательства.
    res9 = cur.execute(
        "SELECT izdatelstvo.id_izdat, avtors.surname FROM books \
        JOIN izdatelstvo ON izdatelstvo.id_izdat = books.id_izdat \
        JOIN avtor_books ON avtor_books.id_book = books.id_book \
        JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor \
        WHERE izdatelstvo.id_izdat = 1").fetchall()
    print(f'9:\n{res9}\n')
    # Получить список всех книг, в названии которых есть заданное слово.
    res10 = con.execute("SELECT nazvanie FROM books WHERE nazvanie LIKE '%для%'").fetchall()
    print(f'10:\n{res10}\n')

# with sq.connect('literature.db') as con:
#     cur = con.cursor()
# Запрос 1
# Обновить год издания всех книг, написанных автором с фамилией "Иванов",
# установив год издания равным 2022:
    # cur.execute(
    #     "UPDATE books SET god_izdan = ? \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE surname = ?))", (2022, 'Иванов'))
    # con.commit()
# Запрос 2
# Обновить название и год издания книги, хранящейся в городе "Москва", установив
# название "Новая книга" и год издания равным 2023:
    # cur.execute(
    #     "UPDATE books SET nazvanie = 'Новая книга', god_izdan = 2023 WHERE mesto_hranen LIKE 'Москва'")
    # con.commit()
# ЗАДАНИЕ 3 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновить название и раздел всех книг, написанных автором с именем "Александр"
# и фамилией "Петров", установив название "Новое название" и раздел
# "Фантастика":
# Запрос 4
# Обновить название всех книг, которые были опубликованы в годы с 2010 по 2015
# включительно, установив название "Старое название":
    # cur.execute(
    #     "UPDATE books SET nazvanie = 'Старое название' WHERE god_izdan >= 2010 AND god_izdan <= 2015")
    # con.commit()
# Запрос 5
# Обновить место хранения всех книг, написанных автором с кодом 7, установив
# место хранения "Библиотека №2"
    # cur.execute(
    #     "UPDATE books SET mesto_hranen = ? \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE id_avtor = ?))", ('Библиотека №2', 7))
    # con.commit()
# ЗАДАНИЕ 6 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновление города из таблицы Издательства по коду города в таблице Книги
# Запрос 7
# Обновление кода автора в таблице АвторКниги по коду автора в таблице Авторы:
    # cur.execute(
    #     "UPDATE avtor_books SET id_avtor = 14 \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE id_avtor = 13)")
    # con.commit()
# ЗАДАНИЕ 8 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновление названия раздела в таблице Книги по названию раздела в таблице Разделы
# ЗАДАНИЕ 9 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновление года издания в таблице Книги по году издания в таблице АвторКниги
# ЗАДАНИЕ 10 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновление места хранения в таблице Книги по названию издательства в таблице 
# Запрос 11
# Обновление фамилии автора в таблице Авторы по коду автора в таблице АвторКниги
    # cur.execute(
    #     "UPDATE avtors SET surname = 'Невский' \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtor_books WHERE id_avtor = 8)")
    # con.commit()
# Запрос 12
# Обновить год издания всех книг, изданных в городе "Москва", на 2022 год.
    # cur.execute(
    #     "UPDATE books SET god_izdan = 2022 \
    #     WHERE id_izdat IN (SELECT id_izdat FROM izdatelstvo WHERE city = 'Москва')")
    # con.commit()
# Запрос 13
# Обновить место хранения всех книг, написанных автором с фамилией "Иванов", на "Книжный шкаф 1"
    # cur.execute(
    #     "UPDATE books SET mesto_hranen = 'Книжный шкаф 1' \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE surname = 'Иванов'))")
    # con.commit()
# Запрос 14
# Обновить год издания всех книг, написанных автором с именем "Анна", на 2023 год.
    # cur.execute(
    #     "UPDATE books SET god_izdan = 2023 \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE name = 'Анна'))")
    # con.commit()
# ЗАДАНИЕ 15 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Обновить название раздела всех книг, изданных в городе "Санкт-Петербург", на "Классика
# Запрос 16
# Обновить год издания всех книг, написанных автором с фамилией "Петров", на 2024 год
    # cur.execute(
    #     "UPDATE books SET god_izdan = 2024 \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE surname = 'Петров'))")
    # con.commit()

# with sq.connect('literature.db') as con:
#     cur = con.cursor() 
# ЗАДАНИЕ 1 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Удалить все записи из таблицы Книги, у которых Раздел = 'Фантастика'
# Запрос 2
# Удалить все записи из таблицы Книги, у которых ГодИздания меньше 2000
    # cur.execute(
    #     "DELETE FROM books WHERE god_izdan < 2000")
    # con.commit()
# Запрос 3
# Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 1
    # cur.execute(
    #     "DELETE FROM avtor_books WHERE id_avtor = 1")
    # con.commit()
# Запрос 4
# Удалить все записи из таблицы Авторы, у которых Фамилия начинается с буквы "А"
    # cur.execute(
    #     "DELETE FROM avtors WHERE surname LIKE 'А%'")
    # con.commit() # Объединен с запросом 15
# Запрос 5
# Удалить все записи из таблицы Издательства, у которых Город равен "Москва"
    # cur.execute(
    #     "DELETE FROM izdatelstvo WHERE city = 'Москва'")
    # con.commit() # Объединен с запросом 14 и 16
# Запрос 6
# Удалить все записи из таблицы АвторКниги, у которых КодКниги равен 10
    # cur.execute(
    #     "DELETE FROM avtor_books WHERE id_book = 10")
    # con.commit()
# Запрос 7
# Удалить все записи из таблицы Книги, у которых МестоХранения равно "Склад"
    # cur.execute(
    #     "DELETE FROM books WHERE mesto_hranen = 'Склад'")
    # con.commit()
# ЗАДАНИЕ 8 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Удалить все записи из таблицы Разделы, у которых Раздел равен "Детективы"
# Запрос 9
# Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 2
    # cur.execute(
    #     "DELETE FROM avtor_books WHERE id_avtor = 2")
    # con.commit()
# ЗАДАНИЕ 10 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# Удалить все записи из таблицы Издательства, у которых Издательство равно "O'Reilly Media"
# Запрос 11
# Удалить все записи из таблицы Книги, у которых Название содержит слово "Война"
    # cur.execute(
    #     "DELETE FROM books WHERE nazvanie LIKE '%Война%'")
    # con.commit()
# Запрос 12
# Удалить все книги, которые были изданы до 2000 года включительно, и которые хранятся в месте хранения "Библиотека №1"
    # cur.execute(
    #     "DELETE FROM books WHERE god_izdan <= 2000 AND mesto_hranen = 'Библиотека №1'")
    # con.commit()
# Запрос 13
# Удалить всех авторов, у которых нет книг в таблице Книги
    # cur.execute(
    #     "DELETE FROM avtors WHERE id_avtor NOT IN (SELECT id_avtor FROM avtor_books)")
    # con.commit()
# Запрос 14
# Удалить все книги, изданные в городе "Москва", из таблицы "Книги"
    # cur.execute(
    #     "DELETE FROM books WHERE id_izdat IN (SELECT id_izdat FROM izdatelstvo WHERE city = 'Москва')")
    # con.commit() # Объединён с запросом 5 и 16
# Запрос 15
# Удалить всех авторов, чьи фамилии начинаются на букву "А" из таблицы "Авторы" и соответствующие записи из таблицы "АвторКниги".
    # cur.execute(
    #     "DELETE FROM avtor_books WHERE id_avtor IN(SELECT id_avtor FROM avtors WHERE surname LIKE 'А%')")
    # cur.execute("DELETE FROM avtors WHERE surname LIKE 'А%'")
    # con.commit() # Объединён с запросом 4
# Запрос 16
# Удалить все записи из таблицы "АвторКниги", связанные с книгами, изданными в городе "Москва"
    # cur.execute(
    #     "DELETE FROM avtor_books \
    #     WHERE id_book IN (SELECT id_book FROM books \
    #     WHERE id_izdat IN (SELECT id_izdat FROM izdatelstvo WHERE city = 'Москва'))")
    # con.commit() # Объединён с запросом 5 и 14
# Запрос 17
# Удалить все книги из таблицы "Книги", которые были написаны авторами, чьи фамилии начинаются на букву "П"
    # cur.execute(
    #     "DELETE FROM books \
    #     WHERE id_book IN (SELECT id_book FROM avtor_books \
    #     WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE surname LIKE 'П%'))")
    # con.commit()
# Запрос 18
# Удалить все книги из таблицы "Книги", которые были изданы в городах, название которых начинается на букву "Н"
    # cur.execute(
    #     "DELETE FROM books \
    #     WHERE id_izdat IN (SELECT id_izdat FROM izdatelstvo WHERE city LIKE 'Н%')")
    # con.commit() # Объединён с запросом 19
# Запрос 19
# Удалить все записи из таблицы "АвторКниги", связанные с книгами, изданными в городах, название которых начинается на букву "Н"
    # cur.execute(
    #     "DELETE FROM avtor_books \
    #     WHERE id_book IN (SELECT id_book FROM books \
    #     WHERE id_izdat IN (SELECT id_izdat FROM izdatelstvo WHERE city LIKE 'Н%'))")
    # con.commit() # Объединён с запросом 18

