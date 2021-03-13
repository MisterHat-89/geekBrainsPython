# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.


class Data:
    __day: int = 0
    __month: int = 0
    __year: int = 0
    __date: str = ""
    __day_in_month: list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @classmethod
    def parse(cls, date: str):
        lister = date.split("-")
        cls.__day = int(lister[0])
        cls.__month = int(lister[1])
        cls.__year = int(lister[2])
        return cls.validate(cls)

    @staticmethod
    def validate(cls) -> str:
        is_day = False
        is_month = False
        is_year = False

        if 1 <= cls.__month <= 12:
            is_month = True
        else:
            return f"Дата {cls.__day}-{cls.__month}-{cls.__year} Невалидна"

        if 1899 <= cls.__year <= 3000:
            is_year = True
        else:
            return f"Дата {cls.__day}-{cls.__month}-{cls.__year} Невалидна"

        if 1 <= cls.__day <= cls.__day_in_month[cls.__month - 1]:
            is_day = True
        else:
            return f"Дата {cls.__day}-{cls.__month}-{cls.__year} Невалидна"

        if is_month & is_year & is_day:
            return f"Дата {cls.__day}-{cls.__month}-{cls.__year} Валидна"


new_date = Data()
new_date2 = Data()

print(new_date.parse("25-3-2020"))
print(new_date2.parse("15-33-2020"))
