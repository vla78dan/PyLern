# print(int("1 cft"))
# print(float("3.14"))
# print(float("vyjuj"))
# print(str(3.14))
# print(str([1, 2, 3]))

price = float(input())
quantity = int(input())
total = price * quantity
print("Количество мороженых: " + str(quantity), "Цена за штуку: " + str(price), "Итоговая стоимость: " + str(total), sep='\n')
