"""
name = input("What is your name? ")
print('Скоро выучит весь питон:',name)
print('Скоро напишет первую игру:',name)
print('Скоро заработает много денег:',name)

course_time = 15
hour_in_day = int(input())
print('Вам потребуется дней:', course_time / hour_in_day)


kinder_price = 60
kinder_piece = int(input())

print('Цена одного киндера:', kinder_price)
print('Сколько вы хотите купить:', kinder_piece)
print('Общая стоимость покупки:', kinder_price * kinder_piece)

kinder_price = 60

print('Стоимость одного киндера:', kinder_price)
print('Стоимость двух киндеров:', kinder_price * 2)
print('Стоимость ста киндеров:', kinder_price * 100)


boss_hp = 1000
ball = 200
lightning = 300
total_pow = (ball * 2) + (lightning * 2)

print('Здоровье босса после атак:', boss_hp - total_pow)


num_of_oper = int(input()) * 20000
num_of_vaccinations = int(input()) * 500
num_of_diss_quadrobers = int(input()) * 2
total = num_of_oper + num_of_vaccinations - num_of_diss_quadrobers
print('Итоговая зарплата:', total)


name = input()
attack_power = int(input())
speed = int(input())
agility = int(input())
level = int(input())

total_pow = ((attack_power * 4) + (agility * 2) + (speed * 3)) * level
print('Имя персонажа:', name)
print('Боеспособность персонажа:', total_pow)

stone = 37
wood = 30
food = 20
build = 90

if build >= 75:
    print('Вы можете построить лабораторию')
if wood >= 25:
    print('Вы можете построить фабрику')
if build >= 100:
    print('Вы можете построить университет')

name_film = input()
genre = input()
reit = int(input())

if genre == 'мелодрама' and reit > 7:
    print('Да, директор заценит!')
else:
    print('Не, это кино директору лучше не предлагать...')



mistake = int(input())
right = int(input())

if mistake == right:
    print('Программист получает квартиру в центре')
else:
    print('Программист без премии, остаётся жить в поместье...')



mistake = int(input())
right = int(input())
day = int(input())
if mistake == right and day < 7:
    print('Программист получает новый айфон!')
else:
    print('Программист остаётся с прошлогодним айфоном...')



course = int(input())
you_rol = int(input())

if course >=1 or you_rol >=7:
    print('Программист получает билет на круиз!')
else:
    print('Программист остаётся без премии на Бали!')


dj_color = input()
up_dress = input()
if dj_color == 'синий' or up_dress == 'синий':
    print('Классный прикид! Проходите в школу')
else:
    print('Увы, в таком виде вам в школу нельзя!')

day_in = int(input())
day_on = int(input())

if day_in >= day_on:
    print('Программисту отправлено 4 банки чёрной икры')
else:
    print('Программист без премии, вынужден питаться фуагрой')

day_in = int(input())
day_on = int(input())
like = input()

if (day_in >= day_on) or like == 'да':
    print('Программист получает новую BMW M5')
else:
    print('Программист продолжает ездить на прошлогодней Audi')


name = input()
genre = input()
if genre == 'рэп' or genre == 'поп':
    print('Мы добавляем в плейлист:', name)
else:
    print('Увы, эта песня не подходит')

food = input()

if food == 'пицца':
    print('Вы получаете сок')
elif food == 'суп':
    print('Вы получаете гренки')
elif food == 'роллы':
    print('Вы получаете соус')
elif food == 'печенька':
    print('Вы получаете мороженое')


    num = int(input())

if num == 1:
    print('Niletto - Любимка')
elif num == 2:
    print('Баста - Медлячок')
elif num == 3:
    print('Instasamka - За деньги да')
elif num == 4:
    print('Anna Asti - Царица')
elif num == 5:
    print('Шаман - Я Русский!')

num = int(input())

if num == 1:
    print('Niletto - Любимка')
elif num == 2:
    print('Баста - Медлячок')
elif num == 3:
    print('Instasamka - За деньги да')
elif num == 4:
    print('Anna Asti - Царица')
elif num == 5:
    print('Шаман - Я Русский!')

food = input()

if food == 'пицца':
    print('Вы получаете сок')
elif food == 'суп':
    print('Вы получаете гренки')
elif food == 'роллы':
    print('Вы получаете соус')
elif food == 'печенька':
    print('Вы получаете мороженое')
else:
    print('Извините, это блюдо мы пока не готовим...')

num1 = int(input())
sign = input()
num2 = int(input())

if sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/':
    print(num1 / num2)
else:
    print('Не знаю такого действия...', 'Чтобы я посчитала, введите: + - * /', sep='\n')


ram_pc = int(input())

if ram_pc >= 1:
    print('Portal2')
if ram_pc >= 2:
    print('Counter-Strike: GO')
if ram_pc >= 4:
    print('Fortnite')
if ram_pc >= 8:
    print('Cyberpunk 2077')

num = int(input())
print(num + 5, num * 2, sep='\n')


num = int(input())
num2 = int(input())
print(num - num2)


n1 = int(input())
n2 = int(input())
print(n1 + n2, n1 * n2, n1, n2)

n1 = int(input())
n2 = int(input())
n3 = int(input())
print(n1 + n2, n3 * n2, sep = '\n')

w1 = input()
n1 = int(input())
n2 = int(input())

print(n1 * 2, n1 * 3, w1)
print(w1, n1 + 2, w1)

num1 = int(input())

if num1 >= 2 and num1<=7:
    print('Лайк от бабули')
else:
    print('Бабуля недовольна!')

num_vk = int(input())
num_tt = int(input())
total = num_vk + num_tt

if total >= 6 and total < 30:
    print('Ого! Вы были активны в соцсетях!')

num = int(input())
if num < 35:
    print('Группа 1')
elif num < 50:
    print('Группа 2')
elif num < 65:
    print('Группа 3')
elif num > 65:
    print('Группа 4')


    num = int(input())
if num < 6:
    print('ночь')
elif num < 12:
    print('утро')
elif num < 18:
    print('день')
elif num < 22:
    print('вечер')
elif num <=23:
    print('ночь')


num = int(input())
if 0 < num < 6:
    print('ночь')
elif num < 12:
    print('утро')
elif num < 18:
    print('день')
elif num < 22:
    print('вечер')
elif num <=23:
    print('ночь')
else:
    print('Ошибка, введите время в часах 0-23.')


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
total = int((num1 + num2 + num3 + num4) / 4)

if total total < 3000:
    print('Пассивно...')
elif total 3000 <= total < 6000:
    print('Нормальная активность')
elif total 6000 <= total < 10000:
    print('Хорошая активность!')
elif total total >= 10000:
    print('Офигенская активность!')


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
total = int((num1 + num2 + num3 + num4) / 4)

if total total < 3000:
    print('Пассивно...')
elif total 3000 <= total < 6000:
    print('Нормальная активность')
elif total 6000 <= total < 10000:
    print('Хорошая активность!')
elif total total >= 10000:
    print('Офигенская активность!')



temp_C = int(input())
if temp_C <= 0:
    cloth = 'пальто и шапка'
if 1 <= temp_C < 15:
    cloth = 'куртка и джинсы'
if temp_C > 15:
    cloth = 'футболка и шорты'
print('Рекомендуемая одежда:', cloth)


"""

# hunger_level = int(input())
#
# # Определяем вариант перекуса
# if hunger_level <= 3:
#     meal = 'яблоко или йогурт'
# elif hunger_level <= 7:
#     meal = 'сэндвич или салат'
# else:
#     meal = 'бургер или шашлык'
#
# # Выводим результат
# print('Ваш обед:', meal)

# # Запрашиваем уровень голода
# hunger_level = int(input())
#
# # Определяем вариант перекуса
# if hunger_level > 6:
#     meal = 'спагетти'
#
# print(meal)


learning = 'обучение не выбрано'










