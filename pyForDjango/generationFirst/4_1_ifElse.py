"""
str = input()
if str == 'a':
    print('ДА!')
else:
    print('NO!')




num = int(input())
first = num // 10
last = num % 10

if first == last:
    print('YES')
else:
    print('NO')


n1, n2, n3 = map(int, input().split())

counter = 0
if n1 % 2 == 0:
    counter += 1
if n2 % 2 == 0:
    counter += 1
if n3 % 2 == 0:
    counter += 1
print(counter)


p1, p2 = input(), input()
if p1 == p2:
    print('Пароль принят')
else:
    print('Пароль не принят')


num = int(input())

if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')


age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

n1 = int(input())
n2 = int(input())
if n1 > n2:
    print(n1)
else:
    print(n2)

a+c = 2b

a = int(input())
b = int(input())
c = int(input())

if a + c == b * 2:
    print('YES')
else:
    print('NO')


1614

num = int(input())

n4 = num % 10
n3 = (num // 10) % 10
n2 = (num // 100) % 10
n1 = num // 1000
if (n1 + n4) == (n2 - n3):
    print('ДА')
else:
    print('НЕТ')

n1 = int(input())
n2 = int(input())
n3 = int(input())

count = 0
if n1 > 0:
    count = count + n1
if n2 > 0:
    count = count + n2
if n3 > 0:
    count = count + n3
print(count)


n1 = int(input())
n2 = int(input())
n3 = int(input())

count = 0
if n1 > 0:
    count = count + n1
if n2 > 0:
    count = count + n2
if n3 > 0:
    count = count + n3
print(count)

age = int(input())
if age <= 13:
    print('детство')
if 24 >= age >= 14:
    print('молодость')
if 59 >= age >= 25:
    print('зрелость')
if age >= 60:
    print('старость')


"""





