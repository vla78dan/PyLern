"""
# var1 = 'hello'
# var2 = 'world'
# var3 = 4
# var4 = 4
# res = var3 + var4
# print(res)
# print(var1 + ' ' + var2)
# print("Результат:" +str(res))

# strip() - возвращает новую строку с удаленными пробельными символами с начала и конца строки.
mess = '   Hello, Bob   '
print(mess.strip()) # Hello, Bob

# Метод strip() также может принимать аргумент, указывающий, какие символы нужно удалить. Если аргумент не указан, по умолчанию удаляются пробельные символы.

mess1 = '---Hello, world!---'
print(mess1.strip('-'))

upper() - используется для преобразования всех символов в строке в верхний регистр.

mess = 'ello, Bob'
mess_up = mess.upper()
print(mess_up) # ELLO, BOB


str1 = str(input())
print(str1)


str1 = str(input())
print(str1[1])

title() - используется для преобразования строки в "титульный регистр", где первая буква каждого слова становится заглавной, а остальные буквы - строчными.

mess ='Hello, world'
mess_title = mess.title()
print(mess_title) # Hello, World

isdigit() -  используется для проверки, состоит ли строка исключительно из цифр. Он возвращает True, если все символы строки являются цифрами, и False в противном случае.
dig_10 = '10354654'
dig_method = dig_10.isdigit()
print(dig_method)

Для того, чтобы посмотреть все методы для типа данных строка, нам необходимо прописать следующее:

str = 'Hello'
print(dir(str))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

Функция dir() возвращает список всех методов и атрибутов, доступных для данного объекта.

метод startswith() - используется для проверки, начинается ли строка с указанного префикса. Он возвращает , если строка начинается с заданного префикса, и False в противном случае. Так же здесь зависимость от регистра, если он не совпадает, то система так же вернет False.

str = 'Hello, world'
res = str.startswith('He') # True
res1 = str.endswith('ld') # True
print(res1)

метод find() - используется для поиска подстроки в строке. Он возвращает индекс первого вхождения указанной подстроки, а если подстрока не найдена, возвращает значение -1.
Он включает в себя:
подстроку (по которой будет осуществляться поиск)
индекс элемента с которого начнет происходить поиск (по дефолту он равен 0 и не обязателен к заполнению)
индекс элемента на котором заканчивается поиск (по дефолту не обязателен к заполнению)

str1 = 'Hello, world'
str_in = str1.find('world') # 7 индекс нахождения подстроки
str_in_2 = str1.find('ld') # 10 индекс нахождения подстроки
str_in_1 = str1.find(' ') # 6 индекс нахождения подстроки
print(str_in_1)



"""



















