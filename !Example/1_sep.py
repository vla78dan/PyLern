print("a", "b", "c", sep=",")      # a,b,c
print("a", "b", "c", sep=".")      # a.b.c
print("a", "b", "c", sep="-")      # a-b-c
print("a", "b", "c", sep="_")      # a_b_c
print("a", "b", "c", sep="\t")     # табуляция: a    b    c
print("a", "b", "c", sep="\n")     # новая строка: каждый аргумент с новой строки
print("a", "b", "c", sep="\r")     # возврат каретки
print("a", "b", "c", sep=" ")      # пробел (значение по умолчанию)
print("a", "b", "c", sep="★")      # a★b★c
print("a", "b", "c", sep="→")      # a→b→c
print("a", "b", "c", sep="❤")      # a❤b❤c
print("a", "b", "c", sep="\\")     # a\b\c
print("a", "b", "c", sep="\"")     # a"b"c
print("a", "b", "c", sep="")       # abc
print("a", "b", "c", sep="   ")    # a   b   c
print("a", "b", "c", sep=", ", end="!\n")  # a, b, c!