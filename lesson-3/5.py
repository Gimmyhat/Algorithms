# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

arr = [randint(-50, 50) for _ in range(10)]
max_negative = max([x for x in arr if x < 0])
print(max_negative, arr.index(max_negative))
