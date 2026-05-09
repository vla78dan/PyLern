"""
count = 5
while count != 0:
    print('Стирка продолжается!')
    count = count - 1
    if count == 0:
        print('stop')



count = 5
while count != 0:
    print('go')
    count = count - 1
    if count == 3:
        print('stop')
        break





count = 1
while count != 5:
    if count == 3:
        print(f'Шаг №{count} был пропущен')
        count = count + 1
        continue
    print(f'Шаг стирки №{count}')
    count += 1



Ваша задача, с помощью цикла while вывести на экран последовательность чисел: 1 2 3 4 5. Нужно выводить по одному числу с каждой итерацией, но так, чтобы все числа оказались на одной строке.
Есть разные способы решения, сделайте так как вам удобно. В конце допускается пробел, например: 1 2 3 4 5 .



count = 1
while count != 6:
    print(count, end=' ')
    count += 1


count = 1
while count <= 20:
    if count % 2 == 0:
        print(count, end=' ')
    count += 1

cont1 = 20
while cont1 >= 1:
    print(cont1, end=' ')
    cont1 -= 1




while True:
    mess = input('Enter a pass:')
    if mess == 'quit':
        break
    else:
        print(mess)
print('Пользователь вышел из чата')
"""












