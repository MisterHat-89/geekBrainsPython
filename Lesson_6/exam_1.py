# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу
# примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class Light:
    __color: str = "Красный"
    time_color = {"Красный": 7, "Жёлтый": 2, "Зелёный": 1}

    def running(self):
        for i in range(6):
            try:
                print(self.__color)
                sleep(self.time_color[self.__color])
                self.__color = list(self.time_color.keys())[list(self.time_color.keys()).index(self.__color) + 1]
            except IndexError:
                self.__color = "Красный"


light = Light()
light.running()
