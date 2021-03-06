# 2. Реализовать класс Road (дорога), в котором определить
# атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы
# асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    _width: int
    _length: int
    _depth: int
    res: int = 25
    _mass: int = 25

    def __init__(self, width: int, depth: int, length: int, ):
        self._depth = depth
        self._width = width
        self._length = length
        self.res = (self._width * self._depth * self._length * self._mass) / 1000


road = Road(20, 5, 5000)
print(f"Result = {road.res} т.")
