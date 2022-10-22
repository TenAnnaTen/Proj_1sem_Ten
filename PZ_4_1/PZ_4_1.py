
while True:
    try:
        x = float(input('Введите веществнное число, модуль котрого < 1: '))
        n = int(input('Введите целое число, большее 0: '))
        if abs(x) < 1 and n > 0:
            a = x
            c = 1
            while c != n + 1:
                b = ((-1 ** n) * (x ** (2 * n + 1)) / (2 * n + 1))
                a += b
                c += 1
            print(f'Приблежённое значение arctg(x): {a}')
            break
        else:
            print('Неправильно введённые данные. Попробуйте ещё раз')
            continue
    except:
        print('Неправильно введённые данные. Попробуйте ещё раз')
        continue