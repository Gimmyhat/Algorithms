# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from collections import Counter

arr = [randint(0, 10) for _ in range(100)]
most_common = Counter(arr).most_common(1)[0]
print(f'Число {most_common[0]} встречается в массиве {most_common[1]} раз(а)')

