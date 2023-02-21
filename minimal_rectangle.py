"""На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
параллельными линиям сетки, покрывающий все закрашенные клетки.
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и
Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника."""


def minimal_rectangle(data):
    horizont = []
    vertical = []
    for i in data:
        horizont.append(i[0])
        vertical.append(i[1])
    min_x = min(horizont)
    min_y = min(vertical)
    max_x = max(horizont)
    max_y = max(vertical)
    return min_x, min_y, max_x, max_y


with open("input.txt", "r") as file:
    data = []
    count = file.readline()
    for line in file:
        data.append([int(x) for x in line.split()])

with open("output.txt", "w") as file:
    file.write(str(minimal_rectangle(data))[1:-1].replace(',', ''))

