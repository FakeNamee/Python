import math
print("Введите координаты первой точки")
a = [int(input("x= ")), int(input("y= "))]

print("Введите координаты второй точки")
b = [int(input("x= ")), int(input("y= "))]

print(math.sqrt((b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2))
