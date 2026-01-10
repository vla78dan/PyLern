"""
print(ord('m'), ord('e'), ord('l'), ord('l'), ord('o')) #72 101 108 108 111
print(chr(65))

sym = input().strip()
code_num = ord(sym)
code_sym = chr(code_num)
print(code_num, code_sym, sep='\n')

sym = input().strip()
code_num = int(ord(sym) + 1)
code_sym = chr(code_num)
print(code_num, code_sym, sep='\n')

str1 = input()
sym_first = ord(str1[0])
sym_last = ord(str1[-1])
sym_mid = str1[1:-1]
print(sym_first, sym_last, sep='\n')
print(f'{sym_first}{sym_mid}{sym_last}')

str1 = input()
str1_a = str(ord('a'))
str1_o = '0'
print(str1.replace('a', str1_a).replace('o', str1_o))

str1 = input()

print(str1
.replace('a',str(ord('a'))).replace('A',str(ord('A')))
.replace('e',str(ord('e'))).replace('E',str(ord('E')))
.replace('i',str(ord('i'))).replace('I',str(ord('I')))
.replace('o',str(ord('o'))).replace('O',str(ord('O')))
.replace('u',str(ord('u'))).replace('U',str(ord('U')))
.replace('y',str(ord('y'))).replace('Y',str(ord('Y')))
)


path = input()

# Заменяем двойные обратные слеши на одинарные
path = path.replace('\\\\', '\\')

# Выводим результат
print(path)
"""




