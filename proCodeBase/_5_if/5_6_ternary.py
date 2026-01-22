"""

num = int(input())
res = 'Большое число' if num > 10 else 'Маленькое число'
print(res)

accuracy_in_percent = float(input())
speed_in_percent = float(input())
res = 'Отличный ИИ' if accuracy_in_percent > 90 and speed_in_percent < 2 else 'Нужно доработать' if accuracy_in_percent <= 90 and speed_in_percent >= 2 else 'Хороший ИИ'
print(res)

temp = int(input())
res = 'Экстремально холодно' if temp < -60 else 'Холодно' if -60 <= temp <= 0 else 'Тепло'
print(res)





"""


num = int(input())
res = num / 2 if num % 2 == 0 else num * 3
print(res)



















