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

s = "Программисты не боятся ошибок. Они просто говорят: 'Это фича!'"
print(s.index('р').swapcase())

s = 'Abracadabra' # Метод .count() позволяет узнать, сколько раз встречается строка
print(s.count('A')) # - 1
print(s.count('ra')) # - 2
print(s.count('a')) # - 4
print(s.count('q')) # - 0

str1 = input()
count_e = str1.count('e')
count_E = str1.count('E')
print(count_e + count_E)



Метод startswith проверяет, начинается ли строка на указанную подстроку. Возвращает True или False.

В первом параметре метода задаем нужную нам подстроку, во втором и третьем необязательных параметрах - индекс начала и конца поиска соответственно.

Метод endswith проверяет, заканчивается ли строка на указанную подстроку и возвращает значения True или False. В первом параметре метода задаем нужную нам подстроку, во втором и третьем необязательных параметрах - индекс начала и конца поиска соответственно.

# Метод .startswith  (с английского «starts with» дословно переводится как «начинаться с») позволяет проверить, начинается ли строка с определенной подстроки (префикса).


str1 = "Oleg Popov"
str_star = str1.startswith('Oleg')
print(str_star)


# Метод .endswith (с английского «ends with» дословно переводится как «заканчиваться чем-то») позволяет проверить, заканчивается ли строка определенной подстрокой.

str1 = "Oleg Popov"
end_star = str1.endswith('pov')
print(end_star)

str1 = input().lower()
print(str1.startswith('mam'))


str1 = input()
post_end = input()
print(str1.endswith(post_end))

str1 = input()
str1_pre = input()
str1_post = input()
print(str1.startswith(str1_pre) and str1.endswith(str1_post))




.ljust() — выравнивание влево;
Метод  .ljust создаст новую строку, в которой исходная строка S прижмется к левой стороне, а справа она будет дополнена символами fillchar до указанной длины width.
d = 'Coldplay'
print(d.ljust(11))
print(d.ljust(14, '-'))
print(d.ljust(14, '$'))
# Coldplay
# Coldplay------
# Coldplay$$$$$$


.rjust() — выравнивание вправо;
Метод  .rjust создаст новую строку, в которой исходная строка S прижмется к правой стороне, а слева она будет дополнена символами fillchar до указанной длины width.
d = 'Coldplay'
print(d.rjust(14))
print(d.rjust(14, '-'))
print(d.rjust(14, '$'))
#       Coldplay
# ------Coldplay
# $$$$$$Coldplay


.center() — центрирование строки;
Метод  .center создаст новую строку, в которой исходная строка S располагается по центру, а слева и справа она будет дополнена символами fillchar до указанной длины width.
Строка 'Coldplay' центрируется, а с обеих сторон добавляются fillchar. Если число добавляемых символов нечётное, больше символов окажется слева.
d = 'Coldplay'
print(d.center(14))
print(d.center(14, '-'))
print(d.center(14, '$'))
print(d.center(15, '%'))
print(d.center(11, '&'))

#    Coldplay
# ---Coldplay---
# $$$Coldplay$$$
# %%%%Coldplay%%%
# &&Coldplay&

.zfill() — дополнение нулями слева.
Метод .zfill возвращает новую строку, в которой исходная строка S дополнена нулями слева так, чтобы длина новой строки стала равна width.
Если параметр width меньше длины строки, то будет возвращена исходная строка без изменений:

d = '123'
print(d.zfill(5))
print(d.zfill(6))
print(d.zfill(7))
print('qwerty'.zfill(14))
# 00123
# 000123
# 0000123
# 00000000qwerty

srt1 = input()
print(srt1.ljust(15, '-'))
srt1 = input()
print(srt1.rjust(10, '!'))

srt1 = input()
print(srt1.center(15, '_'))

print(input().zfill(10))


Метод .islower  имеет следующий шаблон вызова:
S.islower()
Данный метод возвращает True , если строка S не пустая и состоит только из алфавитных букв, записанных в нижнем регистре. Если в строке имеется хотя бы одна заглавная буква, будет возвращено False.  Знаки пунктуации, специальные символы или цифры игнорируются при проверке.

print('qwerty'.islower())
print('qwerty!&&&'.islower())
print('12345'.islower())
print('123qwerty'.islower())
print('123Qwerty'.islower())
# True
# True
# False
# True
# False



Метод .isupper  имеет следующий шаблон вызова:
S.isupper()
Данный метод возвращает True , если строка S не пустая и состоит только из алфавитных букв, записанных в верхнем регистре. Если в строке имеется хотя бы одна строчная буква, будет возвращено False.  Знаки пунктуации, специальные символы или цифры игнорируются при проверке.

print('qwerty'.isupper())
print('QWERTTY'.isupper())
print('QWERTTY%%%%'.isupper())
print('123QWER45687'.isupper())
# False
# True
# True
# True


Метод .isdigit  имеет следующий шаблон вызова:
S.isdigit()
Данный метод возвращает True , если строка S не пустая и состоит только из символов-цифр. В случае, если строка пустая или в строке есть хотя бы один символ отличный от цифр, вернется False

print('123344455'.isdigit())
print('1,2'.isdigit())
print('12Qwww'.isdigit())
print('123 344 455'.isdigit())
print('qwerty'.isdigit())
# True
# False
# False
# False
# False

Метод .isalpha  имеет следующий шаблон вызова:
S.isalpha()
Данный метод возвращает True , если строка S не пустая и состоит только из символов-букв. Если в строке встретится хотя бы один символ, неявляющийся буквой, то метод .isalpha вернет значение False.

print('qwerty'.isalpha())
print('12345687'.isalpha())
print('QWERTY'.isalpha())
# True
# False
# True

Метод .isalnum  имеет следующий шаблон вызова:
S.isalnum()
Данный метод возвращает True , если строка S не пустая и состоит только из букв и цифр. Если в строке имеется хотя бы один не буквенный и не числовой символ, то будет возвращено False:
print('qwerty'.isalnum())
print('qwe123rty'.isalnum())
print('qwe,rty'.isalnum())
print('qwe rty'.isalnum())
# True
# True
# False
# False


Метод .istitle  имеет следующий шаблон вызова:
S.istitle()
Данный метод возвращает True , если строка S не пустая и является строкой заголовков: каждое новое слово начинается с заглавной буквы.  Знаки пунктуации, специальные символы или цифры игнорируются при проверке.

print('Qwerty'.istitle())
print('QwerTy'.istitle())
print('Qw2333erty'.istitle())
print('Qwe,,  rty'.istitle())
# True
# False
# False
# False


"""








































