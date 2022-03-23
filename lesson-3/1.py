# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.
from pprint import pprint

dct = dict.fromkeys(range(2, 100))
for key in dct.keys():
    dct[key] = [x for x in range(2, 10) if key % x == 0]
pprint(dct)