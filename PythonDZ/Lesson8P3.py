class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'{self.quantity + other.quantity}'

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result >= 0:
            return f'{self.quantity - other.quantity}'
        else:
            return 'Разность количества клеток меньше 0'

    def __mul__(self, other):
        return f'{self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'{self.quantity // other.quantity}'

    def make_order(self, count):
        while self.quantity > 0:
            for k in range(1, count + 1):
                print('*', end='')
                self.quantity -= 1
                if self.quantity <= 0:
                    break
            print('\n', end='')


print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(32)
cell3 = Cell(10)
cell4 = Cell(15)
print()
print("Складываем")
print(cell1 + cell2)
print()
print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)
print()
print("Умножаем")
print(cell2 * cell1)
print()
print("Делим")
print(cell1 / cell2)
print()
print("Организация ячеек по рядам")
cell1.make_order(4)
print('\n')
cell2.make_order(16)