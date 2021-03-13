# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    _rows_count: int
    matrix: list
    _view_matrix: str = ""
    _count_number: int = 0

    def __init__(self, lists: list):
        self._rows_count = len(lists)
        if self._rows_count % 2 == 0:
            self._view_matrix = "rectangular"
        if self._rows_count % 3 == 0:
            self._view_matrix = "square"
        self.matrix = lists

    def __str__(self):
        string_matrix = ""
        if self._view_matrix == "":
            return "Its not Matrix"
        if self._view_matrix == "rectangular":
            for i in range(0, len(self.matrix)):
                if i % 2 == 0:
                    string_matrix += "\n"
                string_matrix += f"{str(self.matrix[i])} "
        if self._view_matrix == "square":
            for i in range(0, len(self.matrix)):
                if i % 3 == 0:
                    string_matrix += "\n"
                string_matrix += f"{str(self.matrix[i])} "
        return string_matrix

    def __add__(self, other):
        summary_list = []
        if len(self.matrix) > len(other.matrix):
            self.count_number = len(other.matrix)
        if len(self.matrix) < len(other.matrix):
            self.count_number = len(self.matrix)
        if len(self.matrix) == len(other.matrix):
            self.count_number = len(self.matrix)
        for i in range(0, self.count_number):
            summary_list.append(self.matrix[i] + other.matrix[i])
        return Matrix(summary_list)


print("matrix square")
matrix_square = Matrix([14, 21, 23, 334, 345, 556, 554, 788, 7890])
print(matrix_square)
print()

print("matrix rectangular")
matrix_rectangular = Matrix([14, 21, 23, 334, 345, 556, 554, 788, 7890, 99])
print(matrix_rectangular)
print()

print("matrix summary")
print(matrix_rectangular + matrix_square)
