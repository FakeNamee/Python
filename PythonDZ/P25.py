def convert_binar(value):
    final_list = []
    result = ''
    while value != 0:
        final_list.append(value % 2)
        value = value//2
    final_list = final_list[::-1]
    for j in final_list:
        result = result + str(j)
    return result


a = int(input('Введите число для преобразования в двоичную систему:  '))
print(int(convert_binar(a)))
