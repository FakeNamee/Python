import time as t


def define_the_day(input_day):
    # input_day = int(input('Enter day number: '))
    if input_day > 7 or input_day < 1:
        return 'Введите число от 1 до 7'
    elif input_day == 6 or input_day == 7:
        return "it's weekend!"
    else:
        return "No, it's not weekend"


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

# print(define_the_day())


def sum_of_numbers(number):
    sum = 0
    for value in number:
        if value.isdigit():
            sum += int(value)
    result = round(sum)
    return result


def quarter_position(x, y):
    # x = int(input('X: '))
    # y = int(input('Y: '))
    if x > 0 and y > 0:
        quarter = 1
    elif x < 0 and y > 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    else:
        quarter = 4
    return quarter


class Traffic_light:

    __color = (('Red', 7), ('Yellow', 2), ('Green', 5))

    def running(self):
        for i in self.__color:
            print(i[0])
            t.sleep(i[1])


class My_Class:
    ...