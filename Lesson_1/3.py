# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

x1, y1, x2, y2 = map(int, input('Введите через пробел (x1, y1), (x2, y2): ').split())
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
print(f'y = {k}x + {b}')

# (x1, y1), (x2, y2): 3 4 2 9
# y = -5.0x + 19.0

