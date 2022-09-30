from itertools import count
import os
import random
from msilib.schema import Error
import string
from typing import List


Fatal_Error = True
N = 0
while Fatal_Error != False:
    string = input('Ведите целое число: ')
    try:
        N = int(string)
        Fatal_Error = False
        if N == 0:
            print('Вы ввели 0, пожалуйста введите другое число ')
            Fatal_Error = True
    except ValueError:
        print("Не верный ввод")
List = []
Сomposition = 1
with open('file.txt', 'w') as File:
    Number = random.randrange(1, N)
    for i in range(0, Number):
        File.writelines(str(random.randrange(0, N+1))+'\n')

for i in range(-N, N+1):
    List.append(i)
print(list)

with open('file.txt', 'r') as File:
    for line in File:
        Сomposition *= List[int(line)]
print(f'Произведение элементов на указаных позициях = {Сomposition}')
