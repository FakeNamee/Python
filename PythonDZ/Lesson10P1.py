# Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singletone(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class MyClass(metaclass=Singletone):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'


obj1 = MyClass('Petr', 2)
obj2 = MyClass('Ivan', 15)
obj3 = MyClass('sdxgcfvhjbknml', 3)
print(f'obj1 - {obj1}')
print(f'obj2 - {obj2}')
print(f'obj3 - {obj3}')
obj3.age = 30
print(f'obj3 - {obj3}')
obj4 = MyClass('Karl', 47)
print(f'obj4 - {obj4}')
print(f'obj1 - {obj1}')