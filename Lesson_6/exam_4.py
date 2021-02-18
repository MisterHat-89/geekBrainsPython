# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


from random import randrange


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        self.speed = randrange(1, 40)
        return f" Машина {self.name} поехала "

    def stop(self):
        self.speed = 0
        return " Машина остановилась "

    @staticmethod
    def turn(direction):
        return f" Машина повернула " + direction

    def show_speed(self):
        return f" скорость {self.speed} км/ч"


class TownCar(Car):
    def __init__(self):
        super().__init__("TownCar", "Белый", False)

    def show_speed(self):
        self.speed = randrange(25, 100)
        if self.speed > 60:
            return f" Вы превысили скорость! Скорость {self.speed} км/ч "
        else:
            return f" Скорость {self.speed} км/ч "


class SportCar(Car):
    def __init__(self):
        super().__init__("SportCar", "Красный", False)


class WorkCar(Car):
    def __init__(self):
        super().__init__("WorkCar", "Розовый", False)

    def show_speed(self):
        self.speed = randrange(25, 100)
        if self.speed > 40:
            return f" Вы превысили скорость! Скорость {self.speed} км/ч "
        else:
            return f" Скорость {self.speed} км/ч "


class PoliceCar(Car):
    def __init__(self):
        super().__init__("PoliceCar", "Черный", True)


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

print(f"{sport_car.go()} | {sport_car.turn('Влево')} | {sport_car.show_speed()}")
print(f"{police_car.go()} | {police_car.show_speed()} | {police_car.stop()} | {police_car.show_speed()}")
print(f"{town_car.go()} | {town_car.turn('Назад')} | {town_car.show_speed()}")
print(f"{work_car.go()} | {work_car.turn('Вверх')} | {work_car.show_speed()}")
