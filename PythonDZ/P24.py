First = [1.1, 1.2, 3.1, 5, 10.01]
Second = []
for i in First:
    if i % 1 != 0:
        Second.append(i % 1)
print(Second)
Second.sort()
print(Second)
print(
    f'Разница между максимальным и минимальным значением дробной части элементов = {Second[len(Second)-1]-Second[0]:.2f}')
