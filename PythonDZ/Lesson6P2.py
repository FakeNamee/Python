# Cоздать список от 1 до 100, выбрать числа кратные восьми, возвести их в квадрат и вывести пронумерованный список 
# (map, filtr, list comp, enumerate)
""" newList = list()
iterator = 0
for number in range(1,101):
    if number % 8 == 0:
        newList.append(list([iterator,number*number]))
        iterator += 1

print(newList) """


newlist = list(map((lambda nubmer: nubmer * nubmer), filter(lambda x: (x % 8 == 0), range(1, 101))))
data = list(enumerate(newlist))
print(data)