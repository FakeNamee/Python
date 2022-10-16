#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
#исходной последовательности.
""" import random

intList = []
for listNumber in range(0, 10):
    intList.append(random.randrange(1, 10))
print(intList)

repeatCounter = 0
finalList = list()

for number in intList:
    for checkNumber in intList:
        if number == checkNumber:
            repeatCounter += 1
    if repeatCounter == 1:
        finalList.append(number)
        repeatCounter = 0
    else:
        repeatCounter = 0

print(finalList) """

lst = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
lst = [el for el in lst if lst.count(el) == 1]
print(lst)