print('Введите координаты х и у')
ourList = [int(input()),int(input())]

if ourList[0]>0 and ourList[1]>0:
    print(1)
elif ourList[0]<0 and ourList[1]<0:
    print(3)
elif ourList[0]>0 and ourList[1]<0:
    print(4)
else:
    print(2)