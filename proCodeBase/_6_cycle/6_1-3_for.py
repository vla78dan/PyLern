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

"""








