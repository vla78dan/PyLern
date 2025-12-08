"""
a = 7
b = a
print(a)

a = b = c = 1
print(a, b, c)
print(id(a), id(b), id(c))

a, b = 2.3, 1
print(a, b)
print(id(a), id(b))

a, b = b, a
print(a, b)

print(id(a), id(b))

print(type(a), type(b))

x = 5.8
s = 'Hello'
print(type(x), type(s))


На вход программе подаются две строки (каждая вводится с новой строки). Необходимо их прочитать командами:

s1 = input() # чтение первой строки
s2 = input()

и объединить в одну строку через пробел. Результат вывести на экран.


s1 = input()
s2 = input()
print(s1, s2)
"""

msg = 'brasil'
print(msg.index('ad'))

























