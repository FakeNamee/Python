from random import randint
from typing import List
Imput_error = True
while Imput_error:
    lengt_List = input('Введите длинну списка: ')
    try:
        lengt_List = int(lengt_List)
        if lengt_List <= 0:
            print('Пожалуйста, введите число больше нуля: ')
            Imput_error = True
        else:
            Imput_error = False
    except ValueError:
        print('Ошибочный ввод, введите другое значение')

List = []
for i in range(lengt_List):
    List.append(randint(0, 10))
print(f'Создание списка из {lengt_List} элементов')
print(List)
List_Product = []
if len(List) == 2:
    List_Product.append(List[0]*List[1])
else:
    if len(List) % 2 == 0:
        for i in range(len(List)//2):
            List_Product.append(List[i]*List[len(List)-i-1])
    else:
        for i in range(len(List)//2+1):
            List_Product.append(List[i]*List[len(List)-i-1])

print('Произведение пар чисел')
print(List_Product)
