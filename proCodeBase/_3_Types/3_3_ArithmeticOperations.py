
"""
q = int(input())
w = int(input())
print((q + w), (q - w), (q * w), (q / w))

q = int(input())
w = int(input())
print(q % w)

q = int(input())
w = int(input())
e = int(input())
print((q + w + e) / 3)

a = int(input())
b = int(input())
print(2 * (a + b))

1. Простейшие фигуры:
Квадрат: P = 4a

Прямоугольник: P = 2(a + b)

Треугольник: P = a + b + c

Равносторонний Δ: P = 3a

Круг (длина окружности): C = 2πr = πd

2. Четырехугольники:
Параллелограмм/Ромбоид: P = 2(a + b)

Ромб: P = 4a (частный случай параллелограмма)

Трапеция: P = a + b + c + d

Произвольный n-угольник: P = Σaᵢ (сумма всех сторон)

3. Правильные n-угольники:
Общая формула: P = n·a

n = 3 (треугольник): P = 3a

n = 4 (квадрат): P = 4a

n = 5 (пентагон): P = 5a

n = 6 (гексагон): P = 6a


age = int(input())
print(age * 7)

bananas, monkeys = map(int, input().split())
print(int((bananas / (monkeys * 3))), (bananas % (monkeys * 3)))




P, n, r = map(float, input().split())
print(P * ((1 + (r / 100)) ** n))







"""
ducks, ponds = map(int, input().split())
print((int(ducks / ponds)), (ducks % ponds))
print(*divmod(ducks, ponds))






















