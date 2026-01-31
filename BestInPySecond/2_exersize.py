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




"""
name = input()
genre = input()
if genre == 'рэп' or genre == 'поп':
    print('Мы добавляем в плейлист:', name)
else:
    print('Увы, эта песня не подходит')

















