"""
q = float(input())
print(round(q))


q = float(input())
w = int(input())
print(round(q, w))

q = int(input())
w = int(input())
e = int(input())

print(round(((q + e + w) / 3), 1))

q = int(input())
if q % 2 == 0:
    print("True")
else:
    print("False")

weight = int(input())
print(weight == 0)

q, w = map(int, input().split())

first = w // 100
second = w % 100 // 10
third = w % 10
summ = first + second + third

print(bool(q % summ == 0))

Ракета сможет взлететь, если тяга больше суммы веса ракеты и топлива.

Выведите True, если запуск возможен, и False --> в противном случае.

fuel, weight, thrust = map(int, input().split())
print(thrust > (fuel + weight))

speed = float(input())
in_range = (7.8 <= speed <= 11.2) or (16.5 <= speed <= 25.0)
print(in_range)


"""















































