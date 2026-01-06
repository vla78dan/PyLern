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

hight = float(input())
print(hight >= 160)


a, b, c, d = map(bool, input().split())

print(a == b == c == d)


a, b, c, d = map(bool, input().split())
print(a and b and c and d)

a, b, c, d = input().split()

a = a == "True"
b = b == "True"
c = c == "True"
d = d == "True"

print(a and b and c and d)

data_volume, cpu_load, memory , server_connection = input().split()
data_volume = float(data_volume)
cpu_load = float(cpu_load)
memory = float(memory)
server_connection = bool(server_connection)

print(data_volume <= 1.0 and cpu_load<= 70.0 and memory>= 16.0 and server_connection == True)


q, w, e = map(int, input().split())

print(q > 10 and w > 10 and e > 10)






"""




















