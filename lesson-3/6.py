# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

arr = [randint(0, 100) for _ in range(10)]
max_idx = arr.index(max(arr))
min_idx = arr.index(min(arr))
start_range = min(max_idx, min_idx)
end_range = max(max_idx, min_idx)
print(sum([val for x, val in enumerate(arr) if start_range < x < end_range]))
