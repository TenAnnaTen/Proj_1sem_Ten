class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = 'Line'

    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    # def draw(self):
    #     print('Риосвание прямоугольника')
    ...


# l = Line()
# l.set_coords(1, 2, 3, 4)
# # print(l.__dict__)
# print(l.name)
# l.draw()
#
# r = Rect()
# r.set_coords(5, 6, 7, 8)
# # print(l.__dict__)
# print(r.name)
# # r.draw()


# class Point():
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def set_coord(self, x, y):
#         self._x = x
#         self._y = y
#
#
# pt = Point(1, 2)
# print(pt._x, pt._y)


# class Point():
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def set_coord(self, x, y):
#         if type(x) in (int, float) and type(y) in (int, float):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# pt = Point(1, 2)
# # print(pt.__x, pt.__y)  # нельзя так
# pt.set_coord(100, 20)
# print(pt.get_coord())


# ************************************
# Задача 1
# Создайте класс Person с приватным атрибутом name.
# Реализуйте методы get_name и set_name, которые
# позволяют получать и изменять хзначение этого
# атрибута соответственно.

# class Person:
#     def __init__(self, name='Петя'):
#         self.__name = name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
# pe = Person()
# pe.set_name('Катя')
# print(pe.get_name())


# ********************
# Задача 2
# Создайте класс Car с приватным атрибутом fuel.
# Реализуйте методы get_fuel и set_fuel, которые
# позволяют получить и изменить значение этого
# атрибута соответственною
# При изменении значения fuel проверяйте,
# что оно не старнет меньше нуля.

# class Car():
#     def __init__(self, fuel=7):
#         self.__fuel = fuel
#
#     def set_coord(self, fuel):
#         if fuel >= 0:
#             self.__fuel = fuel
#         else:
#             raise ValueError("Не должно быть меньше 0")
#
#     def get_coord(self):
#         return self.__fuel
#
#
# c = Car()
# c.set_coord(9)
# print(c.get_coord())
# # c.set_coord(-9)


# ******************
# Задача 3
# Создайте класс BankAccount с приватным атрибутами balance и account_number.
# Реализуйте методы get_balance, deposit и withdraw, которые
# позволяют получить текущий баланс, пополнить счет и
# снимать деньги соответственно. При снятии денег
# проверяйте, что на счету достаточно средств для операции.

# class BankAccount:
#     def __init__(self, balance, account_number):
#         self.__balance = balance
#         self.__account_number = account_number
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, x):
#         self.__balance += x
#
#     def withdraw(self, y):
#         if y <= self.__balance:
#             self.__balance -= y
#         else:
#             print('Недостаточно средств')
#
#
# b = BankAccount(2300, 20304)
# print(b.get_balance())
# b.deposit(500)
# print(b.get_balance())
# b.withdraw(400)
# print(b.get_balance())
# b.withdraw(3400)


# *********** ПОЛИМОРФИЗМ **********
class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.h + self.w)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())

geom = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20), Triangle(3, 2, 1), Triangle(4, 3, 2)]

for g in geom:
    print(g.get_pr())



