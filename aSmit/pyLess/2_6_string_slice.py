"""Срезы (или "слайсы") — это мощный инструмент в Python, который позволяет извлекать подстроки из строк. Срезы могут быть использованы для получения части строки, изменения её или даже для работы с другими последовательностями, такими как списки и кортежи.
Рассмотрим синтаксис:
string[start:end:step]
Где:
start — индекс, с которого начинается срез (включительно).
end — индекс, на котором срез заканчивается (исключительно).
step — шаг, с которым выбираются элементы.

Если параметры не указаны, используются значения по умолчанию:
start — 0 (начало строки)
end — длина строки
step — 1 (каждый элемент)




text = 'Hello, World!'
slice_string = text[0:6] # Hello,
print(slice_string)

text1 = 'Hello, World!'
slice_string1 = text[-6:] # World!
print(slice_string1)

text2 = 'Hello, World!'
slice_string2 = text[::2] # World! срез c шагом
print(slice_string2)

text7 = 'Hello, World!'
slice_string3 = text7[:2]  + 'llo'   # Hello
print(slice_string3)

text5 = 'Hello, World!'
slice_string3 = text5[::-1] # !dlroW ,olleH
print(slice_string3)

str1 = input()
print(str1[0:4])

str1 = input()
print(str1[0:4])

str1 = input()
print(str1[::2])

str1 = input()
print(str1[-2:-1])


str1 = input()
str2 = input()
print(str1 + str2)

str1 = input()
str2 = input()
print(str1 * 2 + str2 * 3)

"""

str1 = input()
str2 = input()
print(str1 + ' ' + str2)
