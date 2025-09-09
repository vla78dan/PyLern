"""
q = 4
if q < 0:
    q = -q
    print(q)

a = float(input("a = "))
b = float(input("b = "))
if a < b:
    a, b = b, a
print(a,b)

x = int(input())
if -4 <= x <= 10:
    print("x is between -4 and 10")

x = int(input())
if x:
    print("x is True")

x = int(input())
if True:
    print("x is True")

marks = [3, 3, 4, 3, 4]
if 2 in marks:
    print("будет отчислен")
else:
    print("сдал сессию")

x = int(input())
if x < 0:
    print("отрицательное число")
else:
    print("положительное число")

x = int(input())
if x % 2 == 0:
    print("четное")
else:
    print("не четное")


На вход программе подаются два вещественных числа, записанных в одну строку через пробел. Необходимо их прочитать и вывести на экран наибольшее из этих чисел. Задачу решить с помощью условного оператора.
Sample Input:
8.7 11.0
Sample Output:
11.0



"""
q,w = map(float, input().split())
if q < w:
    print(w)
else:
    print(q)























