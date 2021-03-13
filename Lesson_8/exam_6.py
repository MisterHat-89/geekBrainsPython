# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class NotNumber(Exception):
    def __str__(self):
        return "Это не число"


class Warehouse:
    equips: dict = {"Принтер": [], "Сканер": [], "Ксерокс": []}

    def __init__(self):
        return

    def adding(self, eq):
        self.equips[eq.type_equip].append(eq)

    def __str__(self):
        return f"Наличие на складе принтеров {len(self.equips['Принтер'])} " \
               f"\n Наличие на складе сканеров {len(self.equips['Сканер'])} " \
               f"\n Наличие на складе ксероксов {len(self.equips['Ксерокс'])}"

    def deletes(self, org):
        self.equips[org.type_equip].remove(org)


class Office:
    __equips_office: dict = {"Принтер": [], "Сканер": [], "Ксерокс": []}

    @classmethod
    def movings(cls, org):
        cls.__equips_office[org.type_equip].append(org)
        return cls.reports(org)

    @staticmethod
    def reports(org):
        return f"Перемещение {org.type_equip} в офис проишло успешно"

    @classmethod
    def report_all(cls):
        return cls.rep(cls)

    @staticmethod
    def rep(cls):
        return f"Наличие в офисе принтеров {len(cls.__equips_office['Принтер'])} " \
            f"\n Наличие в офисе сканеров {len(cls.__equips_office['Сканер'])} " \
            f"\n Наличие в офисе ксероксов {len(cls.__equips_office['Ксерокс'])}"


class OfficeEquipment:
    type_equip: str
    firma: str
    sum_equip: int
    color: str


class Printer(OfficeEquipment):
    def __init__(self, firma, sum_equip, color):
        self.type_equip = "Принтер"
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


class Scanner(OfficeEquipment):
    def __init__(self, firma, sum_equip, color):
        self.type_equip = "Сканер"
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


class Xerox(OfficeEquipment):
    def __init__(self, firma, sum_equip, color):
        self.type_equip = "Ксерокс"
        self.firma = firma
        self.sum_equip = sum_equip
        self.color = color

    def __str__(self):
        return f"{self.type_equip} {self.firma} {self.sum_equip} {self.color}"


printers = Printer("HP", "2560", "Белый")
scanners = Scanner("Brother", "1560", "Серый")
xeroxes = Xerox("Agfa", "1166", "Черный")
warehouses = Warehouse()
warehouses.adding(printers)
warehouses.adding(printers)
warehouses.adding(printers)
warehouses.adding(scanners)
warehouses.adding(scanners)
warehouses.adding(xeroxes)
offices = Office

print(warehouses)
type_org = input("Введите тип техники (Сканер, Принтер, Ксерокс): ")

try:
    number = input("Введите количество техники: ")
    if not number.isdigit():
        raise NotNumber()
    number = int(number)

    if len(warehouses.equips[type_org]) >= number:
        for i in range(0, number):
            print(offices.movings(warehouses.equips[type_org][0]))
            warehouses.deletes(warehouses.equips[type_org][0])
        print("*************************")
        print()
        print("---Остатки на складе---")
        print()
        print(warehouses)
        print()
        print("---Остатки в офисе---")
        print()
        print(offices.report_all())
        print("*************************")
    else:
        print()
        print("**Недостаточно оргтехники**")
        print()

except NotNumber as text:
    print(text)
except KeyError:
    print()
    print("**Нет такой техники на складе**")

