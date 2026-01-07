import math

"""
# Ввод угла в градусах

# Преобразование градусов в радианы

# Вычисление синуса

# Вывод результата

angle = math.radians(float(input()))
print(round(math.sin(angle), 5))

print(round(math.sin(math.radians(float(input()))), 5))

print(round(math.pi * math.pow((float(input())), 2), 2))

q = int(input())
w = int(input())
print(math.sqrt(q**2 + w**2))



max_T  = float(input())
min_T = float(input())
print(abs(max_T - min_T))

q = int(input())
w = int(input())
print(math.gcd(q, w))

q=int(input())

print(math.isqrt(q))

q = int(input())

print(math.log(q), math.log10(q), math.exp(math.log(q)), sep='\n')



angle = math.radians(float(input()))
a_sin = round(math.sin(angle), 6)
a_cos = round(math.cos(angle), 6)
a_tan = round(math.tan(angle), 6)
print(a_sin, a_cos, a_tan, sep='\n')


import math

v = float(input())
angle = math.radians(float(input()))
s_angle = math.sin(angle)
g = 9.81

T = (2 * v * s_angle) / g
H = (v ** 2 * s_angle ** 2) / (2 * g)
R = (v ** 2 * math.sin(2 * angle)) / g

print(round(T, 2), round(H, 2), round(R, 2), sep='\n')
v = float(input())
angle = math.radians(float(input()))
s_angle = math.sin(angle)
g = 9.81
T = (2 * v * s_angle) / g
H = ((v ** 2) * (s_angle ** 2)) / 2 * g
R = ((v ** 2) * s_angle) / g
print(round(T, 2), round(H, 2), round(R, 2), sep='\n')


"""


