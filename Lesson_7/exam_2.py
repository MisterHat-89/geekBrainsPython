# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Garments(ABC):
    __V: float = 0
    __H: float = 0

    @property
    @abstractmethod
    def get_consumption(self) -> float:
        pass


class Coat(Garments):

    def __init__(self, v):
        self.__V = v

    @property
    def get_consumption(self) -> float:
        return self.__V / 6.5 + 0.5


class Suit(Garments):

    def __init__(self, h):
        self.__H = h

    @property
    def get_consumption(self) -> float:
        return self.__H * 2 + 0.3


new_coat = Coat(56)
new_suit = Coat(180)

print("Расход ткани для пальто " + "%.2f" % new_coat.get_consumption)
print("Расход ткани для костюма " + "%.2f" % new_suit.get_consumption)
print("Общий расход ткани " + "%.2f" % (new_coat.get_consumption + new_suit.get_consumption))
