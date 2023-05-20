# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figure():  # Родительский класс
    w = int()
    h = int()

    def pr(self):  # метод вычисления периметра
        return (self.w + self.h) * 2

    def sq(self):  # метод вычисления площади
        return self.w * self.h


class Square(Figure):  # подкласс квадрат
    def set_inf(self, a):
        self.a = a

    def pr(self):
        return self.a * 4

    def sq(self):
        return self.a ** 2


class Rectangle(Figure):  # подкласс прямоугольник
    def set_inf(self, w, h):
        self.w = w
        self.h = h


# Проверка
s = Square()
s.set_inf(5)
print(s.pr())
print(s.sq())
r = Rectangle()
r.set_inf(4, 2)
print(r.pr())
print(r.sq())

