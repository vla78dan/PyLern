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


print(q4)