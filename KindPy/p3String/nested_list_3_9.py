
"""
line = [1, 7, 6, 11, 3]
# line - [1, 7, 6, 11, 3]
img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
# img - [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]

# СОЗДАНИЕ многомерного списка, другая запись, делаем копию cgbcrf line[:]
img1 = [line[:], line[:], line[:], line[:], line[:]]
# img1 - [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]

img2 = img[0]  # - [1, 7, 6, 11, 3]
# обращаемся ко второму элементу вложенного списка
img_0_2 = img[0][1]  # 7

img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
img[1] = [0, 0, 0, 0,
          0]  # заменяем значения вложенного списка print(img) [[1, 7, 6, 11, 3], [0, 0, 0, 0, 0], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]

t = [
    ["Люблю", "тебя", "Петра", "творенье"],
    ["Люблю", "твой", "строгий", "стройный", "вид"],
    ["Невы", "державное", "теченье"],
    ["Береговой", "ее", "гранит"]
]
t[0] # ['Люблю', 'тебя', 'Петра', 'творенье']
t[0][2] # Петра
t.append(["Твоих", "оград", "узор", "чугунный"]) # добавляет строчку в список
del t[0][2] # ['Люблю', 'тебя', 'творенье']


На вход программе подаются целые числа, записанные через пробел. Необходимо прочитать эти числа и сохранить в отдельном списке digs. Добавить в конец списка lst список digs отдельным элементом (как вложенный). Результирующий список lst вывести на экран командой:print(lst)

8 11

[5.4, 6.7, 10.4, [8, 11]]
digs = list(map(int, input().split()))
lst = [5.4, 6.7, 10.4]
lst.append(digs)

print(lst)

На вход программе подаются три строки стихотворения (каждая с новой строки). Необходимо прочитать эти строки командами:
s1 = input() # чтение первой строки
s2 = input() # чтение второй строки
s3 = input() # чтение третьей строки

и каждую представить в виде отдельного списка слов (слова разделяются пробелом). Все полученные списки вложить в список lst (образуется двумерный, вложенный список) и вывести его командой:
print(lst)

Мороз и солнце день чудесный
Еще ты дремлешь друг прелестный
Пора красавица проснись

[['Мороз', 'и', 'солнце', 'день', 'чудесный'], ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'], ['Пора', 'красавица', 'проснись']]
"""
s1 = input() # чтение первой строки
s2 = input() # чтение второй строки
s3 = input() # чтение третьей строки

s11 = s1.split()
s21 = s2.split()
s31 = s3.split()
lst = [list(s11), list(s21), list(s31)]
print(lst)




















