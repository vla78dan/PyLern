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

"""



