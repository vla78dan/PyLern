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


"""































