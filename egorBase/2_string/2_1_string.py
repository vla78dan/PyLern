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

str1 = input()
print(str1.isdigit())

str1 = input()
print(str1.isalpha() and str1.islower())


🔹 .strip() — удаляет лишние символы с обоих концов строки;
Порядок символов в строке chars не имеет значения. Например, strip("tir") эквивалентно strip("irt") или strip("rit").
Метод strip() удаляет любые комбинации указанных символов, а не только точные подстроки. То есть он будет удалять символы 't', 'i', и 'r' по отдельности, пока не встретит символ, который не входит в "tir".

🔹 .rstrip() — удаляет символы справа;

🔹 .lstrip() — удаляет символы слева.

Эти методы часто используются при обработке файлов, пользовательского ввода и строковых данных.

s = "   Data Science   "
result = s.strip()
print(result)

s = "ritritAlgorithmtirtir"
print(s.strip("tir"))



Вводится строка, которая может быть окружена символами -, _, !, ?.
Ваша задача — избавиться от символов -, _, !, ? и вывести полученную строку.
str1 = input()
print(str1.strip('-_!?'))
если у кого-то возник вопрос, почему не работает последовательный вызов s.strip('-').strip('_').strip('!').strip('?') ответ в том, что функция strip работает посимвольно,
s.strip([chars])
проверяет каждый символ строки слева есть ли он в chars, как только встречает символ, которого нет в chars, заканчивает проверку слева и проверят справа, там то же самое.
Поэтому если вы делаете проверку сначала на один символ, потом на другой и т.д., то ответ будет не верный.
если chars = '-_!?' , то strip уберет из строки ниже все знаки до буквы q, так как они все входят в chars

!?!?!??!_---____-----qwerty -> qwerty
если strip вызывается сначала для chars = '-', потом для '_', '!', '?'
то получится так:
s.strip('-') #->!?!?!??!_---____-----qwerty (закончит на первом символе слева)
s.strip('_') #->!?!?!??!_---____-----qwerty (закончит на первом символе слева)
s.strip('!') #->?!?!??!_---____-----qwerty (закончит на первом вопросительном)
s.strip('?') #->!?!??!_---____-----qwerty (закончит на первом восклицательном )

str1 = input()
print(str1.lstrip('-_!?'))


name = 'Vladimir'
middle_name = 'Michailovich'
balance_total = 10000000.23
balance = str(balance_total)

text_concat = "Dear " +  name + ' ' + middle_name + ', Your personal account balance is ' + balance + ' $'
print(text_concat)

name = 'Vladimir'
middle_name = 'Michailovich'
balance = 10000000.23

name = 'Vladimir'
middle_name = 'Michailovich'
balance = 10000000.23


text = "Dear {0} {1}, Your personal account balance
is {2} $ ".format(name, middle_name, balance)
print(text) # Dear Vladimir Michailovich, Your personal account balance is 10000000.23 $


name = 'Vladimir'
middle_name = 'Michailovich'
balance = 10000000.23


text = "Dear {name} {middle_name}, Your personal account balance is {balance} $ ".format(name=name, middle_name=middle_name, balance=balance)
print(text) # Dear Vladimir Michailovich, Your personal account balance is 10000000.23 $

name = input()
last_name = input()
print('«Здравствуйте, {last_name} {name}!»'.format(name=name, last_name=last_name))

word = input()
print('Что Вы сказали? {word}? Какое интересное слово'.format(word=word))

num = int(input())
num_q = num - 1
num_l = num + 1
print('Для числа {num} предыдущим будет число {num_q}.'.format(num=num, num_q=num_q))
print('Для числа {num} следующим будет число {num_l}.'.format(num=num, num_l=num_l))
q = float(input())
w = float(input())
e = float(input())


total = (q + w + e) / 3
print('Средний курс доллара за последние три дня: %.2f RUB.' %(total))


name = input()
print(f'Мое имя {name}!')


name = input().upper()
age = int(input())
print(f'Hello {name}. You are {age} years old.')

Напишите программу для перевода натурального значения секунд в значение минут определенного формата (см. тестовые данные).
99 сек - это 1 мин. 39 сек.
sec_ = int(input())
print(f'{sec_} сек - это {int(sec_ // 60)} мин. {sec_ % 60} сек.')

Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. Выведите информацию о разрешении экрана и общее количество пикселей в определенном формате (см. выходные данные в тестах).
Все знаки препинания, пробелы, регистр букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»
Sample Input:
1920 1080
Sample Output:
Разрешение экрана: 1920 x 1080.
Общее количество пикселей = 2073600.
q,w = map(int, input().split())
print(f'Разрешение экрана: {q} x {w}.', f'Общее количество пикселей = {(q * w)}.', sep='\n')

Виды деления
Давайте при помощи F-строк выведем информацию о трех видах деления, которые мы с вами изучили ранее: обычное деление, целочисленное и деление по остатку.
Входные данные
На вход программе поступают два целых числа, при этом гарантируется, что второе число не равно 0.
Выходные данные
Необходимо вывести результат трех видов деления первого числа на второе в определенном формате (см. примеры ниже).
Sample Input 1:
11
5
Sample Output 1:
11 / 5 = 2.2
11 // 5 = 2
11 % 5 = 1
q = int(input())
w = int(input())
print(f'{q} / {w} = {q / w}',f'{q} // {w} = {q // w}',f'{q} % {w} = {q % w}', sep='\n')



Нашей программе поступает на вход x, y, z - три целых числа, обозначающих координаты вектора А. Затем необходимо найти координаты вектора B, путем увеличения на 5 каждой из координат вектора А.
Оба вектора необходимо распечатать в определенном формате.
Sample Input 1:
1
2
3
Sample Output 1:
Vector A(1, 2, 3)
Vector B(6, 7, 8)
x = int(input())
y = int(input())
z = int(input())
print(f'Vector A({x}, {y}, {z})', f'Vector B({x + 5}, {y + 5}, {z + 5})', sep='\n')


Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов (целое число), которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:
Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
You must pay <стоимость>
Sample Input 1:
56.77
11
Sample Output 1:
Current dollar rate is 56.77. You want to buy 11 dollars
You must pay 624.47


exchange_rate = float(input())
quantity = int(input())
print(f'Current dollar rate is {exchange_rate}. You want to buy {quantity} dollars', f'You must pay {(exchange_rate * quantity)}', sep='\n')


x = 7
y = 3
print(f"Результат {x} + {y} = {f"{x + y}"}")


n = 1234
print(f'|{n:7}|')
print(f'|{n:5}|')
print(f'|{n:4}|')
print(f'|{n:2}|')
print(f'|{n:1}|')
# |   1234|
# | 1234|
# |1234|
# |1234|
# |1234|

name = 'Vlad'
print(f'|{name:7}|')
print(f'|{name:5}|')
print(f'|{name:4}|')
print(f'|{name:2}|')
print(f'|{name:1}|')
# |Vlad   |
# |Vlad |
# |Vlad|
# |Vlad|
# |Vlad|

# Символ	Значение
# <	Выравнивает выражение в фигурных скобках по левому краю. У строк такое поведение по умолчанию
# >	Выравнивает выражение в фигурных скобках по правому краю. У чисел такое поведение по умолчанию
# ^	Выравнивает выражение в фигурных скобках по центру

number = 12345.6789
print(f'Число {number = }') #Число number = 12345.6789
print(f'Число |{number:25}|') #Число |               12345.6789|
print(f'Число |{number:<25}|') #Число |12345.6789               |
print(f'Число |{number:>25}|') #Число |               12345.6789|
print(f'Число |{number:^25}|') #Число |       12345.6789        |

text = 'Python 3.12'
print(f'Строка {text = }')#Строка text = 'Python 3.12'
print(f'|{text:<25}|')#|Python 3.12              |
print(f'|{text:>25}|')#|              Python 3.12|
print(f'|{text:^25}|')#|       Python 3.12       |

number = 12345.6789
print(f'Число {number = }') #Число number = 12345.6789
print(f'Число |{number:25}|') #Число |               12345.6789|
print(f'Число |{number:%<25}|') #|12345.6789%%%%%%%%%%%%%%%|
print(f'Число |{number:&>25}|') #Число |&&&&&&&&&&&&&&&12345.6789|
print(f'Число |{number:*^25}|') #Число |*******12345.6789********|



Формат вывода целых чисел
Буква d (от слова decimal) указывает, что число должно быть представлено в десятичной системе счисления.
Для указания минимальной длины и выравнивания целого числа мы используем тот же синтаксис, что и ранее, только в конце добавляем буквы d, явно показывания интерпретатору, что работает в f-строке с целым числом:

number = 12345
print(f'|Число = {number}|')#|Число = 12345|
print(f'|{number:10d}|')#Минимум 10 символов - |     12345|

apple = 'Яблоки'
num = 102
price = 10.4643

print(f'{apple:20s}')# Минимум 20 символов для строки -
print(f'Количество: {num:5d}')# Минимум 5 символов для числа -
print(f'Цена: ${price:>10.2f}')# Выравнивание вправо, 2 знака после запятой

# Яблоки
# Количество:   102
# Цена: $     10.46

Буква d (от слова decimal) указывает, что число должно быть представлено в десятичной системе счисления.

Для указания минимальной длины и выравнивания целого числа мы используем тот же синтаксис, что и ранее, только в конце добавляем буквы d, явно показывания интерпретатору, что работает в f-строке с целым числом:
number = 12345
print(f'Число:{number}')
print(f'|{number:10d}|')# Минимум 10 символов
print(f'|{number:010d}|')# Заполнение нулями (до 10 символов)
print(f'|{number:?<10d}|')# Выравнивание влево, заполнение символами '?' справа
print(f'|{number:!>10d}|')# Выравнивание вправо, заполнение символами '!' слева
print(f'|{number:-^10d}|')# Выравнивание по центру, символы '-' по краям

# Число:12345
# |     12345|
# |0000012345|
# |12345?????|
# |!!!!!12345|
# |--12345---|



Разделители разрядов в числах (d)
При использовании d в f-строках можно влиять на знак разделителя между группами чисел, например, число 1234567 вывести как 1_234_567 или 1,234,567. Здесь числа группируются по три разряда, начиная с конца числа. Это делается для удобства отображения больших чисел.

Для того, чтобы задать разделитель группы, достаточно перед d указать значение символа, который будет отвечать за разделитель:

N = 12345678912345
print(f'{N:,d}')
print(f'{N:_d}')

# 12,345,678,912,345
# 12_345_678_912_345

N = 12345678912345
print(f'{N:,d}')
print(f'{N:_d}')

# 12,345,678,912,345
# 12_345_678_912_345



На вход вашей программе поступают координаты точки x и y - два целых числа, каждое вводится на отдельной строчке.

Ваша задача обязательно сохранить поступающие на вход значения в переменные x и y соответственно, и затем вывести строку вида Точка(x = {значение}, y = {значение})
X = int(input())
Y = int(input())
print(f'Точка(x = {X}, y = {Y})')

Допишите программу, чтобы выводилось только шесть знаков после запятой у переменной number_pi
number_pi = 3.141592653589793
print(f'{number_pi:.6f}')



Но при купле/продаже обычно оставляют только два знака после запятой. В этом и будет заключаться, ваша задача - принять вещественное число, и вывести его в формате двух знаков после запятой
num = float(input())
print(f'{num:.2f}')


Вводится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов под отображение числа. Если в числе не хватает разрядов, необходимо выводить незначащие нули
num = int(input())
print(f'{num:010d}')


num = int(input())
print(f'{num:-^15d}')

Вам необходимо подправить код ниже так, чтобы он выравнивал

первый print по центру
второй print по правому краю
третий print по левому краю
Количество знаков для выравнивания 20 символов, знак разделителя - &

text = input()
print(f"|{text:&^20s}|")
print(f"|{text:&>20s}|")
print(f"|{text:&<20s}|")


"""





























