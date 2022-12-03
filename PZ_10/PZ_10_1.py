# В N колхозах выращивают некоторые сельскохозяйственные культуры из имеющегося
# перечня. Определить культуры, выращиваемые во всех колхозах, и культуры,
# выращиваемые только в некоторых из них.
import random

colh_1 = set()
colh_2 = set()
colh_3 = set()
colh_4 = set()
a = {
    1: 'картофель',
    2: 'пшеница',
    3: 'рожь',
    4: 'ячмень',
    5: 'овес',
    6: 'свекла',
    7: 'подсолнечник',
}
for i in range(0, random.randint(1, 7)):
    colh_1.add(a.get(random.randint(1, 7)))
print(f'Культуры, выращиваемые в 1-ом колхозе:\n{colh_1}')
for i in range(0, random.randint(1, 7)):
    colh_2.add(a.get(random.randint(1, 7)))
print(f'\nКультуры, выращиваемые во 2-ом колхозе:\n{colh_2}')
for i in range(0, random.randint(1, 7)):
    colh_3.add(a.get(random.randint(1, 7)))
print(f'\nКультуры, выращиваемые в 3-ем колхозе:\n{colh_3}')
for i in range(0, random.randint(1, 7)):
    colh_4.add(a.get(random.randint(1, 7)))
print(f'\nКультуры, выращиваемые в 4-ом колхозе:\n{colh_4}')

if (colh_1 & colh_2 & colh_3 & colh_4) == set():
    print('\nВыращиваемых во всех колхозах культур нет')
else:
    print(f'\nКультуры, выращиваемые во всех колхозах: {colh_1 & colh_2 & colh_3 & colh_4}')
