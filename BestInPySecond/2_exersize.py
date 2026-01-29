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





"""

name = input()
attack_power = int(input())
speed = int(input())
agility = int(input())
level = int(input())

total_pow = ((attack_power * 4) + (agility * 2) + (speed * 3)) * level
print('Имя персонажа:', name)
print('Боеспособность персонажа:', total_pow)

























