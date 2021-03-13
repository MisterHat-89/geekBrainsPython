# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    __number: int
    __result: int

    def __init__(self, number):
        self.__number = number
        self.__result = 0

    def __add__(self, other):
        self.__result = self.__number + other.__number
        return self.__result

    def __mul__(self, other):
        self.__result = self.__number * other.__number
        return self.__result

    def __str__(self):
        return f"{self.__result}"


complex1 = Complex(43)
complex2 = Complex(57)
print(complex1+complex2)
print(complex1*complex2)
