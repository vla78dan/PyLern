"""
x = int(input())
if x % 2 ==0:
    if 0 <= x <= 9:
        print("x - цифра")
    else:
        print("x - число")

x = int(input())
if x % 2 == 0:
    if 0 <= x <= 9:
        print("x - цифра")
    else:
        print("x - число")
else:
    print("x - нечетное число")


a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if a > b:
    if a > c:
        print("a -> max")
    else:
        print("c -> max1")
else:
    if b > c:
        print("b -> max")
    else:
        print("c -> max2")
"""
item = int(input())

if item == 1:
    print("Выбран курс по Python")
elif item == 2:
    print("Выбран курс по C++")
elif item == 3:
    print("Выбран курс по Java")
elif item == 4:
    print("Выбран курс по JavaScript")
else:
    print("Неверный пункт")

x = int(input())

if x < 0:
    print("x должно быть положительным")
elif 0 <= x <= 9:
    print("x - цифра")
elif 10 <= x <= 99:
    print("x - двузначное число")
elif 100 <= x <= 999:
    print("x - трехзначное число")













