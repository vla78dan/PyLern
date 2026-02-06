"""
2.1_Сделаем калькулятор, работающий с десятичными числами.
Пользователь вводит:
Первое десятичное число
Знак арифметического действия(+,-,*,/)
Второе десятичное число
Программа должна вывести итоговый результат.

num_fl1 = float(input())
sign = input()
num_fl2 = float(input())

if sign == '+':
    print(num_fl1 + num_fl2)
elif sign == '-':
    print(num_fl1 - num_fl2)
elif sign == '*':
        print(num_fl1 * num_fl2)
else:
    print(num_fl1 / num_fl2)


name = input()
age = int(input())
weight = float(input())

print('Имя:', name)
print('Полных лет:', age)
print('Вес, кг:', weight)

m = int(input())
print('Целых часов:', m // 60)


cake = 50
money = int(input())

if cake <= money:
    print('Вы можете купить пирожков:', money // cake)
else:
    print('К сожалению, у вас не хватает денег')

minut_clock = int(input())
print('Целых часов:', minut_clock // 60)
print('Осталось минут:', minut_clock % 60)


How much does one racket cost?
How much does one ball cost?
How much money does he have in total?
racket_cost = float(input())
ball_cost = float(input())
money_total = float(input())

print('Куплено шариков:', int((money_total - racket_cost) // ball_cost))


Общее количество компов
Количество кабинетов, где нужен всего 1 комп
Количество остальных кабинетов

Total number of computers Number of offices where only 1 computer is needed Number of other offices

total_num_comp = int(input())
only_1_comp = int(input())
other_offices = int(input())
ku = int(total_num_comp - only_1_comp)

print('Всего было компов:', total_num_comp)
print('Кабинетов с 1 компом:', only_1_comp)
print('В оставшиеся кабинеты поставили по:', int(ku // other_offices))
print('Вернули директору:', int(ku % other_offices))
"""




