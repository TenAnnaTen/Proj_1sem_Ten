# class Point:
#
#     "Класс для представления координат точек на плоскости"
#
#     color = 'red'
#     circle = 2

# после объявления класса он образовал пространство
# имён Point, в к-ом есть две переменные


# print(Point.color)
# print(Point.circle)
# print(Point.__dict__)

# *******************
# Создание экземпляров класса

# pointOne = Point()
# print(pointOne.circle)
# print(pointOne.__dict__)

# pointTwo = Point()
# print(pointTwo.color)
# print(pointTwo.__dict__)

# **********************
# изменение значений свойств класса Point

# Point.circle = 3
# print(Point.circle)
# print(pointTwo.circle)

# **********************
# изменение значений свойств класса pointOne

# pointOne.color = 'green'
# print(pointOne.color)
# print(pointTwo.color)
# print(pointOne.__dict__)

# ***************************
# добавление новых свойств класса Point
#
# Point.hiddens = False
# Point.inher = True
# print(Point.__dict__)
# print(pointOne.hiddens)
# print(pointTwo.inher)

# ****************
# удаление атрибута из класса

# del Point.hiddens
# print(Point.__dict__)

# **********************
# функция getattr - позволяет проверить наличия атрибута у класса
# print(getattr(pointTwo, 'hiddens', False))
# print(getattr(pointTwo, 'inher', False))

# **********************
# перед удалением необходимо проверить его наличие\отсутсвие
# print(hasattr(Point, 'circle'))

# if hasattr(Point, 'inher'):
#     del Point.inher

# print(Point.__dict__)

# *************************
# Еще раз о пространстве имен
# проверим пространста имен у экземпляров

# print(pointOne.__dict__)
# print(pointTwo.__dict__)
# они пустые

# **************************
# добавим в класс pointOne собственный атрибут like

# pointOne.like = True
# print(pointOne.__dict__) # в пространстве имен класса pointOne появилось локальное свойство like

# *************8
# изменим свойство circle
# pointOne.circle = 5
# print(pointOne.circle)

# ****************
# теперь удалим  свойство circle из класса pointOne
# del pointOne.circle  # свойство удаляется из собственного пространства имен класса pointOne
# print(pointOne.circle)  # и замещается свойством из класса Point

# print(Point.hiddens == False)
# print(Point.__doc__)


# ****** МЕТОДЫ КЛАССОВ. АТРИБУТ self *************

# class Point:
#
#     "Класс для представления координат точек на плоскости"
#
#     color = 'red'
#     circle = 2
#
#     #  создание методов
#     #******************
#     # метод назначения координат
#     def set_coords(self, x=0, y=0):
#         print("вызов метода set_coords для " + str(self))
#         self.x = x
#         self.y = y
#
#     # метод получения координат
#     def get_coords(self):
#         print("вызов метода get_coords для " + str(self))
#         return (self.x, self.y)
#
#
# pointOne = Point()
#
# # вызов метода
# # pointOne.set_coords(10, 20)
# # print(pointOne.__dict__)
#
# # если при вызове не передаются значения, то подставятся начения по умолчанию
# # pointOne.set_coords()
# # print(pointOne.__dict__)
#
# # pointTwo = Point()
# # pointTwo.set_coords(100, 200)
# # print(pointOne.__dict__)
#
# # print(pointTwo.get_coords())


# ********************** 1 *************

# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

# class TriangleChecker:
#     a = int()
#     b = int()
#     c = int()
#
#     def dlin_triangle(self, a=2, b=2, c=4):
#         print("вызов метода set_coords для " + str(self))
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         a, b, c = self.a, self.b, self.c
#         if type(a) == int and type(b) == int and type(c) == int:
#             if a >= 0 and b >= 0 and c >= 0:
#                 if a + b > c and c + b > a and a + c > b:
#                     return "-Ура, можно построить треугольник!"
#                 else:
#                     return "-Жаль, но из этого треугольник не выйдет!"
#             else:
#                 return "-С отрицательными числами ничего не выйдет!"
#         else:
#             return "-Нужно вводить только числа"
#
#
# q = TriangleChecker()
# q.dlin_triangle(0, 4, 6)
# print(q.is_triangle())

# ************************* 2 *************

# Есть класс Person, конструктор которого принимает три
# параметра (не учитывая self) – имя, фамилию и квалификацию
# специалиста. Квалификация имеет значение заданное по
# умолчанию, равное единице.
#  У класса Person есть метод, который возвращает строку,
# включающую в себя всю информацию о сотруднике.
#  Класс Person содержит деструктор, который выводит на экран
# фразу "До свидания, мистер …" (вместо троеточия должны
# выводиться имя и фамилия объекта).

# class Person:
#     name = str()
#     surname = str()
#     qualif = int()
#
#     def dann(self, name, surname, qualif=1):
#         self.name = name
#         self.surname = surname
#         self.qualif = qualif
#
#     def vozv(self):
#         return f'Имя: {self.name}, Возраст: {self.surname}, Квалификация: {self.qualif}'
#
#     def Del(self):
#         print(f'До свидания, мистер {self.name} {self.surname}')
#         if hasattr(Person, self.name) and hasattr(Person, self.qualif):
#             del self.name
#             del self.surname
#             del self.qualif
#
#
# w = Person()
# w.dann('Пётр', 'Иванов', 4)
# w.Del()

# ********************************* 3 ****************
# Николай – оригинальный человек.
# Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
# Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
# В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет,
# а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено,
# даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство
# «отчество» или метод «приветствие», то ничего у такого хитреца не получится).
# class Nikola:
#     __slots__ = ['name', 'old']
#
#     def dann(self, name, old):
#         self.name = name
#         self.old = old
#         if self.name != 'Николай':
#             first_name = self.name
#             self.name = f'Я не {first_name}, а Николай!'
#         else:
#             pass
#
#
# N = Nikola()
# N.dann('Николай', 7)
# print(N.__slots__)


# *************************** 4 *******************
# Создайте клас Список, который имеет методы
# для добавления и удаления элементов,
# поиска элемента и сортировки списка
# Создать экземпляр класса и выполнить в нем:
# 1. Заполнить список 15 рандомными элементами
# 2. Проверить наличие в списке элемента со значением 2 и удалить его
# 3. Выполнить сортировку

# import random
#
#
# class Spisok:
#     def zap_many(self, z):
#         self.lst = [random.randint(1, 100) for i in range(0, z)]
#
#     def zap(self, n):
#         self.lst.append(n)
#
#     def udal(self, u):
#         self.lst.remove(u)
#
#     def sear(self, p):
#         if p in self.lst:
#             print(f'Значение {p} встречается {self.lst.count(p)} раз')
#         else:
#             print('Нет такого элемента')
#
#     def sor(self):
#         self.lst.sort()
#
#
# s = Spisok()
# s.zap_many(14)
# print(s.__dict__)
# s.zap(2)
# print(s.__dict__)
# s.sear(2)
# s.udal(2)
# print(s.__dict__)
# s.sor()
# print(s.__dict__)
