import random 
import os

print('Создание алгортма перемешивания списка','\n')
n = int (input('Укажите размер списка: '))
list_primordial = list([random.randint(1,66) for i in range(0, n)])
print(f'\nИзначальный список:\t{list_primordial}')
random.shuffle(list_primordial)
print(f'Перемешанный список:\t{list_primordial}')
