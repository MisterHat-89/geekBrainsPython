# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Table:
    _length: int
    _width: int
    _height: int
    _name: str

    def __init__(self, length, width, height, name):
        self._length = length
        self._width = width
        self._height = height
        self._name = name

    def result(self):
        return f"Стол {self._name}, Длина {self._length}, Ширина {self._width}, Высота {self._height}"


table_kit = Table(115, 125, 150, "Кухонный")
table_room = Table(145, 125, 145, "Комнатный")

print(f"{table_kit.result()}")
print(f"{table_room.result()}")
