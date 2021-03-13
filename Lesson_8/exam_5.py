# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.


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
    equips_office: dict = {"Принтер": [], "Сканер": [], "Ксерокс": []}

    @classmethod
    def movings(cls, org):
        cls.equips_office[org.type_equip].append(org)
        return cls.reports(cls)

    @staticmethod
    def reports(cls):
        return f"Наличие в офисе принтеров {len(cls.equips_office['Принтер'])} " \
            f"\n Наличие в офисе сканеров {len(cls.equips_office['Сканер'])} " \
            f"\n Наличие в офисе ксероксов {len(cls.equips_office['Ксерокс'])}"


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
print()
print("**Перемещение принтера**")
print(offices.movings(warehouses.equips["Принтер"][0]))
print()
warehouses.deletes(warehouses.equips["Принтер"][0])
print(warehouses)
print("*******************************")
print("**Перемещение сканера**")
print(offices.movings(warehouses.equips["Сканер"][0]))
warehouses.deletes(warehouses.equips["Сканер"][0])
print()
print(warehouses)
print("*******************************")
