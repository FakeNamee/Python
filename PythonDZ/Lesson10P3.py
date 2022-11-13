class TypeDescriptor:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]


class Stationery:

    title = TypeDescriptor('title')

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой!')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом!')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером!')


# obj_stationary = Stationery('Канцелярская принадлежность')
obj_pen = Pen('pen')
# obj_pencil = Pencil('Карандаш')
# obj_handle = Handle('Маркер')


# obj_stationary.draw()
obj_pen.draw()
print(obj_pen.title)
# obj_pen.title = '12'
# print(obj_pen.title)
# del obj_pen.title

# obj_pencil.draw()
# obj_handle.draw()