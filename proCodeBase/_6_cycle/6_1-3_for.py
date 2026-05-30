"""
word = 'Python'
for letter in word:
    print(letter)

numbers = [1, 2, 3]
for number in numbers:
    print(number)

person = {"name": "Natasha", "age": 18}
for key, value in person.items():
    print(f'{key}: {value}')

# name: Natasha
# age: 18



unique_num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for num in unique_num:
    print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


for i in range(10):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(10, 15):
    print(i)

# 10
# 11
# 12
# 13
# 14

for i in range(2, 10, 2):
    print(i)
# 2
# 4
# 6
# 8


for i in range(10, 2, -2):
    print(i)

# 10
# 8
# 6
# 4



hunters = ['Djin', 'Don', 'Bobbb', 'Dodd']

name_to_find = "Don"

for hunter in hunters:
    if hunter == name_to_find:
        print(f'{name_to_find} in list')
        break
else:
    print(f'{name_to_find} is not in list')

# Don in list


num = 17

for i in range(2, num):
    if num % i == 0:
        print(f'{num} не является простым числом')
        break
else:
    print(f'{num} простое число')

# Вывод:
#
# 17 — простое число!
#
# Здесь else сработал, потому что число не делилось ни на одно значение из диапазона.



for i in range(5): # Внешний цикл (строки)
    for j in range(3): # Внутренний цикл - столбцы
        print('?', end='') # Вывод звездочек
    print() # Переход на новую строку

# ???
# ???
# ???
# ???
# ???


for i in range(3):
    if i == 1:
        continue

else:
    print("Цикл завершился без break")

# Здесь else выполнится, потому что break ни разу не случился.

for i in range(5, 5):
    print("Это не выведется")

else:
    print("Ни одной итерации не было")

Задача 1. Напишите программу, которая запрашивает у пользователя число и с помощью цикла for выводит все числа от 1 до введённого числа (включительно).

num = int(input())
for i in range(1, num + 1):
    print(i)



    Запрашиваем у пользователя число и выводим все чётные числа от 1 до этого числа включительно с использованием цикла for и range().

num = int(input())
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)
_______________________________________________________________________________

Задача 3. Сумма от 1 до n

🎯 Задание
Считай одно целое число n. Выведи сумму всех чисел от 1 до n включительно, используя цикл for и range().
Если n < 1, выведи 0.

Требования:
использовать for и range(); вывод -- одно число.
🧪 Пример ввод
-5
🧪 Пример вывод
0

n = int(input())

summ = 0
if n < 1:
    print(0)
else:
    for i in range(1, n + 1):
        summ += i
    print(summ)

Считай с клавиатуры число --> сколько названий будет введено.
Затем считай указанное количество строк --> названия фруктов.
Выведи те названия, длина которых больше 5 символов (каждое с новой строки).
🧪 Пример ввода:
4
яблоко
груша
ананас
банан
🧪 Пример вывода:
яблоко
ананас

n = int(input())

for i in range(n):
    name = input()
    if len(name) > 5:
        print(name)

n = int(input())

for i in range(n):
    ticket = int(input())
    if 'A' in ticket:
        print(ticket)

Считай с клавиатуры одну строку --> текст заклинания.

Выведи все гласные из списка a, e, i, o, u, y (учитывая обе раскладки --> строчные и заглавные) в порядке появления в исходной строке, без пробелов и прочих символов.

🧪 Пример ввода:

Azaroth summons Umbra


🧪 Пример вывода:

AaouoUa

str1 = input()

str_word = 'aeiouyAEIOUY'

result = ''

for char in str1:
    if char in str_word:
        result += char
print(result)


n = int(input())

summ_n = 0
if n < 1:
    print(0)
else:
    for i in range(1, n + 1):
        summ_n += i

print(summ_n)
____________________________________________________________
Считай с клавиатуры строку --> текст заклинания.
Раздели текст на слова.
Выведи через пробел каждое второе слово, начиная со второго (2-е, 4-е, 6-е и т. д.).
🧪 Пример ввода:
Lux veritas umbra vitae sanguis
🧪 Пример вывода:
veritas vitae

str1 = input().split()
result = []
for i in range(len(str1)):
    if i % 2 == 1:
        result.append(str1[i])
print(' '.join(result))
_______________________________________________________________________________
Считай с клавиатуры сначала одно целое число --> сколько чисел будет введено.
Затем считай указанное количество целых чисел (каждое на новой строке).
Определи, сколько из них чётные, а сколько нечётные.
Выведи два числа (каждое с новой строки):
количество чётных;
количество нечётных.
🧪 Пример ввода:
3
1
2
3
🧪 Пример вывода:
1
2

n = int(input())
even_count = 0
odd_count = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count, sep='\n')

_________________________________________________________
Считай с клавиатуры одно целое число --> количество танков.
Затем считай стоимости каждого танка (каждое значение на новой строке).
Подсчитай общую стоимость и выведи сумму.
🧪 Пример ввода:
5
100
200
300
400
500
🧪 Пример вывода:
1500
n = int(input())

price_t_summ = 0
for i in range(1, n + 1):
    price_t = int(input())
    price_t_summ += price_t
print(price_t_summ)
_____________________________________________________________________________

Считай с клавиатуры одно целое число --> количество танков в бою.
Затем считай уровни каждого танка (каждое значение на новой строке).
Подсчитай, сколько танков имеют уровень 8 или выше, и выведи это число.
🧪 Пример ввода:
10
8
9
5
6
9
10
4
8
9
10
🧪 Пример вывода:
7

tank_in_fight = int(input())
level_tank_summ = 0

for i in range(1, tank_in_fight + 1):
    level_tank = int(input())
    if level_tank >= 8:
        level_tank_summ += 1
print(level_tank_summ)

"""





































