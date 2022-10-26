from abc import ABC, abstractmethod


class ClothCalculation(ABC):
    @abstractmethod
    def calculate(self):
        pass

    @staticmethod
    def calculate_parameters(cloth_list):
        cloth_expenses_sum = 0
        for cloth in cloth_list:
            cloth_expenses_sum = cloth_expenses_sum + cloth.calculate()
        return cloth_expenses_sum


class Cloth(ClothCalculation):
    def __init__(self, cloth_type, parameter):
        self._cloth_type = cloth_type
        self._parameter = parameter

    def __add__(self, other):
        return self.calculate() + other.calculate()

    @property
    def cloth_type(self):
        return self._cloth_type

    @cloth_type.setter
    def cloth_type(self, new_cloth_type):
        self._cloth_type = new_cloth_type

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, new_parameter):
        self._parameter = new_parameter

    def calculate(self):
        if self._cloth_type.lower() == "coat":
            return self._parameter / 6.5 + 0.5
        if self._cloth_type.lower() == "costume":
            return self._parameter * 2 + 0.3


coat = Cloth("coat", 10)
costume = Cloth("costume", 9)

clothes = [coat, costume]
print(ClothCalculation.calculate_parameters(clothes))

print(coat + costume)