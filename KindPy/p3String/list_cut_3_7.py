lst = ['Moscow', 'Ufa', 'Tver', 'Kazan']
lst1 = lst[1: 3] # ['Ufa', 'Tver']
lst2 = lst[2:] # ['Tver', 'Kazan'] - выделяет элементы со второго до конца списка
lst3 = lst[:3] # ['Moscow', 'Ufa', 'Tver']
city = lst[:] # ['Moscow', 'Ufa', 'Tver', 'Kazan'] - получаем копию списка
city_id = id(city) # 1568304545728 - ['Moscow', 'Ufa', 'Tver', 'Kazan'] переменные ссылаются на разные списки
lst_id = id(lst) # 2530710983040 - ['Moscow', 'Ufa', 'Tver', 'Kazan'] переменные ссылаются на разные списки
city_copy = list(city) # - ['Moscow', 'Ufa', 'Tver', 'Kazan'], создаем копию списка
lst_link = lst # - ['Moscow', 'Ufa', 'Tver', 'Kazan'], создает ссылку на список с тем же ID
marks = [2, 3, 4, 3, 5, 2] # [2, 3, 4, 3, 5, 2]
marks1 = marks[2: -1] # [4, 3, 5]
marks2 = marks[-3:-1] # [3, 5]
marks3 = marks[1:5:2] # [3, 3] - срез
marks4 = marks[:5:2] # [2, 4, 5] - срез
marks5 = marks[1::2] # [3, 3, 2]
marks7 = marks[::2] # [2, 4, 5]
marks8 = marks[::-1] # [2, 5, 3, 4, 3, 2] берем все элементы начиная с последнего до начала списка
marks9 = marks[::-2] # [2, 3, 3] берем все элементы начиная с последнего, через один до начала списка

# - изменение группы элементов
marks = [2, 3, 4, 3, 5, 2] # [2, 3, 4, 3, 5, 2]
marks[2:4] = ['good', 'not good']
# print(marks) - [2, 3, 'good', 'not good', 5, 2]
marks [2:4] = 10, 20 # [2, 3, 10, 20, 5, 2]




print(marks)