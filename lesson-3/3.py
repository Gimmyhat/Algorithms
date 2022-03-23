# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

arr = [randint(0, 100) for _ in range(10)]
max_idx = arr.index(max(arr))
min_idx = arr.index(min(arr))
arr[max_idx], arr[min_idx] = arr[min_idx], arr[max_idx]
