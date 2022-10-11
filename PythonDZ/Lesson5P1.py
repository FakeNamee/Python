List = []


with open("TEXTABV.txt", "r", encoding="utf-8") as f:         # Открываем файл для чтения
    # считываем из файловой переменной строку (автоматически обрезаем '\n' в конце строки) и записываем в список
    List = [line.rstrip() for line in f]

print(List)
List = [line.replace('абв', '   ') for line in List]
print(List)
