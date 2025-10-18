# my_list = ["one", "two", "three"]
# print(my_list[0])
# another_list = ["five", "six", "seven"]
# anyList = my_list + another_list
# print(anyList)
# anyList[0] = "One cap of tea"
# print(anyList)
# anyList.append("ten")
# print(anyList)
# any_list_pop = anyList.pop()
# print(any_list_pop)
# print(anyList)

super_list = ["one", "111111", "three", 'five', '55', 'seven', '20.25558']
print(super_list)
super_list_pop = super_list.pop(1)
print(super_list)
print(super_list_pop)
super_list.sort()
print(super_list)
super_list.sort(reverse=True)
print(super_list)

"""
Вложенные списки
Прекрасная особенность структур данных в Python состоит в том, что они могут быть вложенными (nested). Это значит, что мы можем создавать структуры данных внутри структур данных. Например: список внутри списка.
Давайте посмотрим, как это работает!
"""
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
matrix = [lst1, lst2, lst3]
print(matrix)
print(matrix[2][1])

"""

# Генераторы списков (List Comprehensions)
В Python есть возможность создавать списки с помощью генераторов списков (List Comprehensions). Этот термин трудно перевести на русский язык, иногда его ещё переводят как "абстракция списков" или "списковое включение". Генераторы списков позволяют быстро создавать списки. 
"""

first_col = [row[0] for row in matrix]
print(first_col)
















