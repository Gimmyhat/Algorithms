# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

matrix = [[randint(0, 10) for _ in range(5)] for _ in range(5)]
# транспонируем матрицу, чтобы искать минимальное значение по строкам
matrix_trans = [list(row) for row in zip(*matrix)]
print(max([min(row) for row in matrix_trans]))
