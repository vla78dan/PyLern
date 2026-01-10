"""
name = input()
adress = input()
number = input()

print(f'Здравствуйте, {name}! Ваш заказ №{number} будет доставлен по адресу: {adress}.')

code_str = input()
year = int(input())
num = int(input())
region = int(input())

print(f'Трек-номер: {code_str}-{year:02d}-{num:04d}-{region:02d}')


weight_post = float(input())
price_post = float(input())
pay_pr = int(input())

base_post = weight_post * price_post
sum_post = (base_post * pay_pr) / 100
total_post = base_post + sum_post

print(f'Вес: {weight_post} кг. Базовая стоимость: {base_post:.2f} руб. Надбавка: {sum_post:.2f} руб. Итог: {total_post:.2f} руб.')


km = int(input())
base_price = int(input())
fix_price = int(input())

variable_cost = km * base_price
total_cost = variable_cost + fix_price

print(f'Лог: distance_km={km}, base_price={base_price}, variable_cost={variable_cost}, fixed_fee={fix_price}, total_cost={total_cost}')


"""

price_post = float(input())
nds_in_pr = int(input())
sum_post = price_post * (nds_in_pr / 100)
total_post = price_post + sum_post

print(f'Стоимость без НДС: {price_post:.2f} руб. НДС: {sum_post:.2f} руб. Итоговая стоимость: {total_post:.2f} руб.')


















