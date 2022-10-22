while True:

    try:
        A = float(input('Введите число, большее 1: '))

        if A > 1:
            b = 1
            K = 2

            while b <= A:
                b += 1 / K
                K += 1

            b -= 1 / K
            K -= 2
            print(f'K = {K}. Сумма: {b}')
            break

        else:
            print('Число не больше 1')
            continue

    except:
        print('Неверно введённые данные')
        continue