# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".

class Tovar:
    name = str()
    price = float()
    kolvo = int()

    def set_inf(self, name, price, kolvo):
        if type(name) == str and type(price) in (float, int) and type(kolvo) == int:
            self.name = name
            self.price = price
            self.kolvo = kolvo
        else:
            print('Введите правильные значения')

    def get_inf(self):
        print(f'Название: {self.name}, Цена: {self.price}, Количество: {self.kolvo}')


t = Tovar()
t.set_inf('каша', 34, 67)
t.get_inf()
