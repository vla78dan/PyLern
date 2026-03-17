"""

i = 1
while i <= 10:
    print(i, end=' '))
    i = i + 1
#1 2 3 4 5 6 7 8 9 10

i = 1
while i < 6:
    print('hello', end=' ')
    i = i + 1
#hello hello hello hello hello


i = 20
while i > 10:
    print(i, end=' ')
    i = i - 1
20 19 18 17 16 15 14 13 12 11


a = int(input())
while a != 0:
    print('Повторите ввод')
    a = int(input())



guess = input()
password = 'qwerty'
while guess != password:
    print('Введите верный пароль')
    guess = input()





guess = input()
password = 'qwerty'
count = 0
while guess != password:
    count += 1
    print('Введите верный пароль')
    guess = input()
print(f'Вы ввели пароль', count, 'раза')


a = [1, 2, 33] * 5
print(a)
count = 0
while 33 in a:
    count += 1
    a.remove(33)
    print(count)
    print(a)

[1, 2, 33, 1, 2, 33, 1, 2, 33, 1, 2, 33, 1, 2, 33]
1
[1, 2, 1, 2, 33, 1, 2, 33, 1, 2, 33, 1, 2, 33]
2
[1, 2, 1, 2, 1, 2, 33, 1, 2, 33, 1, 2, 33]
3
[1, 2, 1, 2, 1, 2, 1, 2, 33, 1, 2, 33]
4
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 33]
5
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]


alpha = 3
while alpha <= 24:
    print(alpha)
    alpha *= 2
    print(alpha)

i = 25
while i >= 14:
    print(i)
    i = i - 1

i = 25
while i >= 14:
    print(i)
    i = i - 1
"""

