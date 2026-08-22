"""
num = int(input())
if 100 <= num <= 999:
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')


Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
num = int(input())
n3 = num % 10
n2 = num % 100 // 10
n1 = num // 100
if n1 != n2 and n1 != n3 and n2 != n3:
    print('Цифры различны')
else:
    print('Цифры не различны')



n = 147
q = n % 100 // 10
w = n // 100
print(q, w)

print(81 %9
      )

x = int(input())
if -1 <= x <= 17:
    print('Принадлежит')
else:
    print('Не принадлежит')


x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')



a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print('YES')
else:
    print('NO')


"""

