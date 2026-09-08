"""



total_n = 0

for i in range(4):
    money = int(input())
    total_n += money
print(total_n)


total_spend = 0
for i in range(5):
    spend = int(input())
    total_spend += spend
print(total_spend)




count_spent = int(input())
total_spend = 0

for i in range(count_spent):
    spend = int(input())
    total_spend += spend
print(total_spend)

str1 = input()
num1 = int(input())

for i in range(num1):
    print(str1)



str1 = input()
str2 = input()
str3 = input()
num = int(input())
for i in range(num):
    print(str1, str2, str3, sep='\n')



bal = 1000
for i in range(5):
    oper = input()
    summ_oper = int(input())
    if oper == 'списание':
        bal -= summ_oper
    elif oper == 'зачисление':
        bal += summ_oper
print(f'Ваш итоговый баланс: {bal}')


bal = 1000
for i in range(5):
    oper = input()
    summ_oper = int(input())
    if oper == 'зачисление':
        bal += summ_oper
    if oper == 'списание' and (summ_oper < bal):
        bal -= summ_oper
    else:
        print('Списание невозможно, недостаточно средств')

print(f'Ваш итоговый баланс: {bal}')

bal = 1000

for i in range(5):
    oper = input()
    summ_oper = int(input())
    if oper == 'зачисление':
        bal += summ_oper
    elif oper == 'списание':
        if summ_oper <= bal:
            bal -= summ_oper
        else:
            print('Списание невозможно, недостаточно средств')
print(f'Ваш итоговый баланс: {bal}')


bal = 0

n_income = int(input())
n_outcome = int(input())
for i in range(n_income):
    bashli_income = int(input())
    bal += bashli_income
for i in range(n_outcome):
    bashli_outcome = int(input())
    bal -= bashli_outcome
print(f'Ваш итоговый баланс: {bal}')

"""
verno = 0
for i in range(6):
    str1 = input()
    if str1 == "искусство":
        verno += 1
print(f"Правильно введённых слов: {verno}")



