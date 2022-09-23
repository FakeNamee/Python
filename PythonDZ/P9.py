print ('Введите номер четверти координатной оси от 1 до 4')
quarter = int(input())
match quarter:
    case 1:
        print("x(1,Infinity), y(1,Infinity)")
    case 2:
        print("x(1,-Infinity), y(1,Infinity)")
    case 3:
        print("x(1,-Infinity), y(1,-Infinity)")
    case 4:
        print("x(1,Infinity), y(1,-Infinity)")
