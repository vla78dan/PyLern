"""
name = 'Bobb'
age = 22

print('My name is {} and i am {} years old.'.format(name, age))

value = 3.14159
print("PI: {:.2f}".format(value))
print("PI: {:.2f}".format(value))
print("PI: {:.3f}".format(value))

name = input()
age = input()
town = input()
print("Привет, {}! Тебе уже {} лет, и ты живешь в {}.".format(name, age, town))

num = float(input())
q = int(input())
print("{:.{q}f}".format(num, q=q))

name = input()
age = input()
hobby = input()
print("Меня зовут {name}, мне {age} лет, и я люблю {hobby}.".format(name=name, age=age, hobby=hobby))


name = input()
age = input()
print(f'Меня зовут {name}, мне {age} лет.')

"""
# name = input()
# age = input()
# print(f'Фильм {name} был выпущен в {age}.')

# print(chr(128512))

# sym = input()
# num_sym = ord(sym)
# chr_sym = chr(num_sym)
# print(num_sym, chr_sym, sep='\n')

# text = "  a   b\tc\n"
# result = " ".join(text.split())
#
# print(result)

# text = "abba"
# print(text)
# print(ord("A"))
# print("" or "guest")
# print([] and 123)
# color = "red"
#
# match color:
#     case c:
#         print("Захватили:", c)
#
#         raw = "   "
#
#         if (name := raw.strip()):
#             print(f"Привет, {name}")
#         else:
#             print("Имя не введено")
#




raw = "   "

if (name := raw.strip()):
    print(f"Привет, {name}")
else:
    print("Имя не введено")

score = 72

label = "зачёт" if score >= 60 else "незачёт"
print(label)
