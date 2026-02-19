"""
q = 'Я стану крутым программистом!'
print(q, q, q, sep='\n')

str1 = input()
num1 = int(input())
print(str1 * num1)

print('Лев Николаевич Толстой написал "Война и мир"')

q = input()
w = input()
print(q)
print(w)

q = input()
w = input()
e = input()
print(e)
print(w)
print(q)

str1 = input()
print((str1 + ' ')* 4)

str1 = input()
print(len(str1))

str1 = input()
str2 = input()
print(str1 + str2)




print('Гараж' in not 'Гараж')



str1, str2, str3 = map(str, input().split())
q = str(ord(str1))
w = str(ord(str2))
e = str(ord(str3))
print('Код символа ' + str1 + ' равен ' + q)
print('Код символа ' + str2 + ' равен ' + w)
print('Код символа ' + str3 + ' равен ' + e)



str1, str2, str3 = map(str, input().split())
q = str(ord(str1))
w = str(ord(str2))
e = str(ord(str3))
print('Код символа ' + str1 + ' равен ' + q)
print('Код символа ' + str2 + ' равен ' + w)
print('Код символа ' + str3 + ' равен ' + e)


str1 = input()
print(str1[0])


str1 = input()
print(str1[-1])


s = 'qwerty123'
print(s[5:2])


str1 = input()
print(str1[:4])


str1 = input()
print(str1[-5:])


s = 'qwerty123'

print(s[::-1])
print(s[:])
print(s[::2])
print(s[5:2])

s = 'qwerty123'

# print(s[7:4:-1]) #21y
print(s[4:7:-1]) #Пустая строка
print(s[-2::-2])
# print(s[5:2])

str1 = input()
print(str1[1::2])

str1 = input()
print(str1[::-1])

str1 = input()
print(str1[-1::-3])

str1 = input()
print(str1[-1] + str1[0:-1])

str1 = 'HELLO world'
print(str1.upper()) # HELLO WORLD
print(str1.lower()) # hello world
print(str1.count('l')) # количество 'l' - 1
print(str1.find('l')) # индекс подстроки - 9
print(str1.rfind('l')) # индекс подстроки справа - 9
print(str1.find('z')) # несуществующий символ возвращает (-1)
#print(str1.index('z')) # несуществующий символ возвращает Error
print(str1.replace('L', 'WWW')) # HEWWWWWWO world
print(str1.isalpha()) # состоит ли строка из только букв False, тк есть пробел
print(str1.isdigit()) # состоит ли строка из только цифр False

str1 = '111'
print(str1.rjust(5, '0')) # -00111 дополняет строку справа до указанной длины
print(str1.ljust(7, '9')) # -1119999


q = 'ivanov ivan ivanovich'
print(q.split()) #- ['ivanov', 'ivan', 'ivanovich'] - разбивает строку по пробелам и сохраняет в список
print(len(q.split())) #- 3
print(q.split('n')) # - ['iva', 'ov iva', ' iva', 'ovich']? разбиваем по букве n

w = '12.3665.456523.4587.654'
t = w.split('.')
print(t) # - ['12', '3665', '456523', '4587', '654']
print('='.join(t)) # - 12=3665=456523=4587=654
e = '   jhlkj         '
print(e.strip()) # - jhlkj удаляет пробелы
print(e.lstrip()) # -'jhlkj         '
print(e.rstrip()) # - '   jhlkj'

string.upper() - переводит все буквы в верхний регистр
string.lower() - переводит все буквы в нижний регистр
string.capitalize() - переводит первую букву слова в верхний регистр, а все остальные в нижний
string.title() - переводит первую букву каждого слова в верхний регистр, а все остальные в нижний
string.swapcase() - меняет регистр всех букв в тексте
string.strip() - удаляет пробелы в начале и конце строки
string.lstrip() - удаляет пробелы в начале строки
string.rstrip() - удаляет пробелы в конце строки
string.count('substring') - возвращает количество вхождений подстроки в тексте
string.replace('old_substring', 'new_substring') - заменяет вхождения подстроки на новую в тексте
string.find('substring') - возвращает индекс первого вхождения подстроки в тексте, если не найден - возвращает -1
string.index('substring') - возвращает индекс первого вхождения подстроки в тексте, если не найден - вызывает ValueError

string.split('delimiter') - возвращает список, разделенный по указанному разделителю
string.join(list) - возвращает новую строку, в которой все элементы из списка string объединены в одну строку

str1 = input()
print(str1.upper())

str1 = input()
print(str1.lower())

str1 = input()
print(str1.swapcase())

text = 'каска'
print(text.rfind('а'))

str1 = input()
print(str1.replace('z', '').replace('w', ''))

s = input().lower()
s = s.replace('o', '').replace('a', '').replace('y', '').replace('e', '').replace('i', '').replace('u', '')

print('.' + '.'.join(s))
"""




























