"""
user_input = input("Enter a string: ")
if len(user_input) > 5:
    print('Строка длиннее пяти символов')

if(user_input := input("Enter a string: ")) and len(user_input) > 5:
    print('Строка длиннее пяти символов')

temp = int(input())
speed = int(input())
sound_cyborg = int(input())

if(total := temp > 100 and speed > 30 and sound_cyborg > 70):
    print('Ловушка активирована!')
else:
    print('Ловушка не активирована. Киборг спасен!')


if str1 := input().strip() == 'да':
    print('Вы фанат Сумерок!')
elif str1 == 'нет':
    print('Не всем нравится!')
else:
    print("Пожалуйста, введите 'да' или 'нет'.")


num = int(input())
if number:= num % 2 == 0:
    print(f'Число {num} четное.')
else:
    print(f'Число {num} четное.')




nickname = input()

# Проверяем все условия
if (nickname and
    nickname[0].isupper() and
    all(c.isalnum() or c == '_' for c in nickname) and
    len(nickname) <= 20):
    print(True)
else:
    print(False)
"""







































