"""
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(my_dict['key1'])

price_shop = {
    "apple": 2.99,
    "oranges": 1.99,
    "milk": 5.80
}
print(price_shop["milk"])

d = {
    "k1": 123,
    "k2": [0,1,2],
    "k3": {"inside_key": 100 }
}

print(d['k2'][1])
print(d['k3']['inside_key'])

d_ex = {

    "k2": [0,1,2],
}

print(d_ex["k2"][1])


my_dict = {
    "key1": 123,
    "key2": [12,23,33],
    "key3": ['item0', 'item1', 'item2'],
}
print(my_dict['key3'])
print(my_dict['key3'][0].upper())

my_dict['key1'] = my_dict['key1'] - 123
print(my_dict)

d = {

}

d['animal'] = 'dog'
d['name'] = 'Bobbbbbb'
d['age'] = 53

print(d)

d = {
    "key1": {'nestkey': {'subnestkey': 'value'}}
}
print(d['key1']['nestkey'])

"""
d = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}
# Метод, который возвращает список всех ключей
d_keys = d.keys()
print(d.keys()) #dict_keys(['key1', 'key2', 'key3'])
print(d.values()) # dict_values([1, 2, 3])

# Метод, возвращающий кортежи (tuples) для всех элементов
print(d.items()) # dict_items([('key1', 1), ('key2', 2), ('key3', 3)])























