# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    __count_cells: int = 0

    def __init__(self, count: int):
        self.__count_cells = count

    def __add__(self, other):
        return Cell(self.__count_cells + other.__count_cells)

    def __sub__(self, other):
        if self.__count_cells - other.__count_cells < 0:
            return "Вычесть невозможно"
        return Cell(abs(self.__count_cells - other.__count_cells))

    def __mul__(self, other):
        return Cell(self.__count_cells * other.__count_cells)

    def __truediv__(self, other):
        return Cell(self.__count_cells // other.__count_cells)

    def make_order(self, length: int):
        string_list = ""
        for i in range(0, self.__count_cells):
            if i % length == 0:
                string_list += "\n"
            string_list += "*"
        return string_list


new_cell = Cell(15)
new_cell2 = Cell(10)
add_cell = Cell(0)
sub_cell = Cell(0)
mul_cell = Cell(0)
truediv_cell = Cell(0)

add_cell = new_cell + new_cell2
sub_cell = new_cell - new_cell2
mul_cell = new_cell * new_cell2
truediv_cell = new_cell / new_cell2

print("Первая ячейка")
print(new_cell.make_order(5))
print()
print("Вторая ячейка")
print(new_cell2.make_order(3))
print()
print("Сложение")
print(add_cell.make_order(3))
print()
print("Разность")
print(sub_cell.make_order(7))
print()
print("Умножение")
print(mul_cell.make_order(9))
print()
print("Деление")
print(truediv_cell.make_order(8))
print()
