from cmath import pi


Imput_error = True
print('Введите точность вывода числа π. Пример d = 0.001')
while Imput_error:
    str1 = input('d = ')
    try:
        d = float(str1)
        if d <= 0:
            print('Введите число больше 0   ')
            Imput_error = True
        else:
            Imput_error = False
    except ValueError:
        print("Это не правильный ввод, попоробуйте снова")

Pi = str(pi)


if d % 1 == 0:
    Step = 0
else:
    Step = len(str1) - str1.find('.') - 1


Npi = float(Pi[:Step+2:])
print(Npi, '    ', type(Npi))
