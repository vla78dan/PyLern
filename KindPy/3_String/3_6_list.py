"""
q = ["Moscow", "Tver", "Vologda"]
print(q)
marks = [2, 3, 4, 3, 5, 2]
print(marks[0])
# средний балл
marks_midlle = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]) / 6
print(marks_midlle)
marks_last = marks[-1] # 2
print(marks_last) # 4-21

print(marks_midlle)


lst2 = [1, 2.5, [-1, -2, -3], 4]
print(lst2)

q = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
print(q)

marks = [2, 3, 4, 3, 5, 2]
marks[1] = "удовлетворительно"
print(marks) # [2, 'удовлетворительно', 4, 3, 5, 2]
print(len(marks)) # 6



t = [23.5, 25.6, 27.3, 26.0, 30.4, 29.5]
print(t) # [23.5, 25.6, 27.3, 26.0, 30.4, 29.5]
print(min(t))  # 23.5
print(max(t))  # 30.4
print(sum(t))  # 162.3 summa
print(sum(t)/len(t))  # 27.05 среднее значение

# функция sorted, если ее вызвать с одним аргументом:
# sorted(t)
# то она возвратит новый список с отсортированными значениями по неубыванию (или, как часто говорят, по возрастанию). И, обратите внимание, эта функция не меняет прежний список t, она именно возвращает новый список с отсортированными значениями. Очевидно, чтобы сохранить результат работы этой функции, следует использовать переменную, например, так:

t1 = sorted(t) # [23.5, 25.6, 26.0, 27.3, 29.5, 30.4] возвращает новый список, отсортированный по возрастанию
t2 = sorted(t, reverse=True) # [30.4, 29.5, 27.3, 26.0, 25.6, 23.5] возвращает новый список, отсортированный по убыванию.

s = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
q = sorted(s)
print(max(s)) # y
print(min(s)) # h
print(q) # ['h', 'n', 'o', 'p', 't', 'y']

l1 = [1, 2, 3]
l2 = [4, 5]
l3 = l1 + l2  # [1, 2, 3, 4, 5]
l4 = ["i", "love", "python"]  # ['i', 'love', 'python']

l5 = l4 * 2  # ['i', 'love', 'python', 'i', 'love', 'python']
print(l5)
l7 = ["i"] + ["love"] + ["python"]  # ['i', 'love', 'python']
l8 = ["i"] + ["love"] * 3 + ["python"]  # ['i', 'love', 'love', 'love', 'python']

lst = ["Москва", 1320, 5.8, True, "Тверь", False] # ['Москва', 1320, 5.8, True, 'Тверь', False]
l2 = 1320 in lst # True
l2 = 132 in lst # False

lst = ["Москва", 1320, 5.8, True, "Тверь", False, [1, 2]] # ['Москва', 1320, 5.8, True, 'Тверь', False, [1, 2]]
l3 = [1, 2] in lst # True


"""



lst = ["Москва", 1320, 5.8, True, "Тверь", False, [1, 2]] # ["Москва", 1320, 5.8, True, "Тверь", False, [1, 2]]
del lst[2] # ['Москва', 1320, True, 'Тверь', False, [1, 2]]


print(lst)











