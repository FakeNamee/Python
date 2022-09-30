from ast import Num

num = input("Введите число: ")
sum = 0
for i in str(num):
    if i != "." and i != "-":
        sum += int(i)
print(sum)
