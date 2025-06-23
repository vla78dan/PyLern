#\n  символ перевода строки

q = "panda\nneeds"
# panda
# needs

q1 = "\tpanda\nneeds\npython" # \t - табуляция
#	panda
#needs
#python

q2 = "panda\\needs\\ python" # \\ - экранирование
#panda\needs\ python
#путь к файлуF:\Py\3129\PyLern\KindPy\p3String
q3 = "F:\\Py\\3129\\PyLern\\KindPy\\p3String"
#console
#F:\Py\3129\PyLern\KindPy\p3String

q4 = r"F:\\Py\\3129\\PyLern\\KindPy\\p3String" # row строка - сырая строка выводит так, как записано в строке, игнорируя спецсимволы
#console
#F:\\Py\\3129\\PyLern\\KindPy\\p3String



q8 = input()
#print(q8.replace(" ", "\\"))


#На вход программе подается строка со словами, разделенными пробелами (один пробел между соседними словами). #В строке может присутствовать от одного и более слов. Необходимо прочитать строку и первый пробел (если он #есть) заменить на одинарную кавычку, а все остальные - на двойные. Результирующую строку вывести на #экран.
#My best friend is Python!
#My'best"friend"is"Python!

q11 = input().split()
print('"'.join(q11))

#print(q12.replace("\" ", "'", 1))

















