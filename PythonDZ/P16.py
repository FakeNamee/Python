from multiprocessing.sharedctypes import Value


while True:
    num = input('Введите положительное целое число ')
    try:
        num = int(num)
        if num > 0:
            break
        else:
            print('Вы ввели отрицательное число ')
    except ValueError:
        print('Eror. Введите целое число ')

list = []
for i in range(1, num + 1):
    num = round(((1+1/i)**i),2)
    list.append(num)
print(list)
print(f'Сумма последовательности числе = {sum(list)}')    
