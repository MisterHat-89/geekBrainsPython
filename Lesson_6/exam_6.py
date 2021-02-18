# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер).
# каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str

    @staticmethod
    def draw():
        return "Запуск отрисовки"


class Pen:

    def __init__(self):
        self.title = "ручка"

    def draw(self):
        return f"Запуск отрисовки для {self.title}"


class Pencil:

    def __init__(self):
        self.title = "карандаш"

    def draw(self):
        return f"Запуск отрисовки для {self.title}"


class Handle:

    def __init__(self):
        self.title = "маркер"

    def draw(self):
        return f"Запуск отрисовки для {self.title}"


pen = Pen()
pencil = Pencil()
handle = Handle()

print(f"{pen.draw()}")
print(f"{pencil.draw()}")
print(f"{handle.draw()}")
