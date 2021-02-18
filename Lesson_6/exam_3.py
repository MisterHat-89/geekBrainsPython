# 3. Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        string = f"{self.surname} {self.name}"
        return string

    def get_total_income(self, rand):
        self._income["wage"] = 5000 * rand
        self._income["bonus"] = 1000 * rand
        return self._income["wage"] + self._income["bonus"]


one = Position("Виктория", "Белогородова", "Пайтон разработчик")
two = Position("Максим", "Заборов", "Пайтон тестировщик")
three = Position("Филипп", "Забулдыга", "Пайтон разработчик")

print(f"ФИО: {one.get_full_name()} - Деньги: {one.get_total_income(1)} руб.")
print(f"ФИО: {two.get_full_name()} - Деньги: {two.get_total_income(0.5)} руб.")
print(f"ФИО: {three.get_full_name()} - Деньги: {three.get_total_income(0.2)} руб.")
