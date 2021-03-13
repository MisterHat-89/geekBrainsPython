# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self):
        return


class OfficeEquipment:
    type_equip: str
    firma: str
    sum_equip: int
    color: str


class Printer(OfficeEquipment):
    def __init__(self, type_equip, firma, sum_equip, color):
        self.type_equip = type_equip
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


class Scanner(OfficeEquipment):
    def __init__(self, type_equip, firma, sum_equip, color):
        self.type_equip = type_equip
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


class Xerox(OfficeEquipment):
    def __init__(self, type_equip, firma, sum_equip, color):
        self.type_equip = type_equip
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


printers = Printer("HP", "Принтер", "2560", "Белый")
scanners = Scanner("Brother", "Сканер", "1560", "Серый")
xeroxes = Xerox("Agfa", "Ксерокс", "1166", "Черный")

print(printers)
print(scanners)
print(xeroxes)

