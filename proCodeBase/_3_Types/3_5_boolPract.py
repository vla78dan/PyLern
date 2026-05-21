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



Задача 6. Делится ли на сумму цифр
📜 История:
На математическом кружке задали задачу: дано два числа. Первое --> любое целое, второе --> всегда трёхзначное и положительное. Нужно проверить, делится ли первое число на сумму цифр второго.

🎯 Задание:
Считайте с клавиатуры два целых числа в одной строке через пробел:

a, b = map(int, input().split())

Второе число (b) гарантированно трёхзначное (от 100 до 999).

Найдите сумму его цифр.

Проверьте, делится ли a на эту сумму без остатка.

Выведите True, если делится, и False если нет.

Не используйте условные операторы (if).

🧪 Пример ввода:

18 123


🧪 Пример вывода:

True

# a, b = map(int, input().split())
#
# b1 = b // 100
# b2 = (b // 10) % 10
# b3 = b % 10
#
# print((b1+b2+b3) % a == 0)


a, b = map(int, input().split())

# Находим цифры трёхзначного числа b
b1 = b // 100  # первая цифра (сотни)
b2 = (b // 10) % 10  # вторая цифра (десятки)
b3 = b % 10  # третья цифра (единицы)

# Сумма цифр числа b
sum_digits = b1 + b2 + b3

# Проверяем, делится ли a на сумму цифр без остатка
# Результат (True или False) выводим сразу
print(a % sum_digits == 0)


Считайте с клавиатуры три целых положительных числа:

fuel, mass, thrust = map(int, input().split())


где:

fuel --> масса топлива в тоннах,

mass --> масса ракеты в тоннах,

thrust --> подъёмная сила в условных единицах.

Будем считать, что ракета сможет взлететь, если значение thrust больше суммы mass и fuel.

Выведите True, если запуск возможен, и False --> в противном случае.

Решите задачу без использования условных операторов (if).

fuel, mass, thrust = map(int, input().split())
print(fuel + mass < thrust)

В центре обработки данных установлен искусственный интеллект, который приступает к анализу только при идеальных условиях. Перед запуском нужно убедиться, что:

Объём данных не превышает 1 ТБ.

Загрузка процессора не более 70%.

Доступная память не меньше 16 ГБ.

Соединение с сервером активно.

Если хоть одно из условий не выполняется --> запуск откладывается.

🎯 Задание:
Считайте с клавиатуры четыре значения через пробел:

data_volume --> объём данных в ТБ (вещественное число);

cpu_load --> загрузка процессора в процентах (вещественное число);

memory --> доступная память в ГБ (вещественное число);

server_connection --> наличие соединения с сервером (True или False).

Выведите True, если все условия выполнены, иначе --> False.

🧪 Пример ввода:

1.0 70 16 True


🧪 Пример вывода:

True

data_volume, cpu_load, memory, server_connection = input().split()
data_volume = float(data_volume)
cpu_load = float(cpu_load)
memory = float(memory)
server_connection = bool(server_connection)

print(data_volume <= 1.0 and cpu_load <= 70.0 and memory >= 16.0 and server_connection == True)
"""
a, b, c = map(int, input().split())
print(a > 10 and b > 10 and c > 10)
