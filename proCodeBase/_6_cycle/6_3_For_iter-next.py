"""
for line in iter(input, 'stop'):
    print(line)

s = "cat"

it = iter(s)

print(next(it))
print(next(it))
print(next(it))
c
a
t


r = range(5)
it = iter(r)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
0
1
2
3
4

it = iter('abcd')

first = next(it)
print(first)

for ch in it:
    print(ch)

n = 5
it = iter(range(n))
next(it)
second = next(it)

print(second)

_____________________________________________________________________________
Шаг 1. Считайте строку s .

Шаг 2. Выделите первый символ строки и оставшуюся часть.

Шаг 3. Выведите две строки:
first=<...>
tail=<...>

Шаг 4. Контракт: после выполнения должны существовать s, first, tail.

Важно: проверка ожидает, что в решении используются iter() и next().


s = input()
it = iter(s)
first = next(it)
tail = ''.join(it)
print(f'first={first}')
print(f'tail={tail}')

Раннее утро, туман над взлётной полосой. По краям стоят маяки с номерами: 0, 1, 2, 3… Бортовой компьютер проверяют простым тестом: нужен именно второй маяк на маршруте, потому что по нему чаще всего видно, что счётчик «сдвинулся» правильно.
Иногда маршрут слишком короткий. Тогда тест не должен ломаться, он должен честно сказать: «второго маяка нет».
🎯 Задание
Шаг 1. Считайте целое число n (n может быть 0).
Шаг 2. Рассмотрите последовательность 0, 1, 2, ..., n-1. Найдите её второй элемент. Если второго элемента нет, ответом считается строка "none".
Шаг 3. Выведите: second=<...>
Шаг 4. Контракт: после выполнения должны существовать n, second.
Важно: проверка ожидает, что в решении используются iter() и next().
Нажмите, чтобы увидеть тестовые данные
Тестовые данные
№ Теста
Входные данные
5
Выходные данные
second=1
n = int(input())
if n <= 1:
    second = 'none'
else:
    it = iter(range(n))
    first = next(it)
    second = next(it)
print(f'second ={second}')
"""
s = input()  
k = int(input())
it = iter(s)
try:
    for _ in range(k):
        next(it)

    rest_chars = []
    try:
        while True:
            rest_chars.append(next(it))
    except StopIteration:
        pass
    
    rest = ''.join(rest_chars)
except StopIteration:

    rest = ""


if rest == "":
    print("rest=<empty>")
else:
    print(f"rest={rest}")





























