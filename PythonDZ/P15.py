N = int(input('Введите число N: '))
value = 1
c = []
for i in range(1, N+1):
    value *= i
    c.append(value)
print(c)
