"""
t_july = [20, 25, 32, 36, 42, 48, 56, 60] #[20, 25, 32, 36, 42, 48, 56, 60]

a = [True, False, 25, 25.23, 'hello', True, [1, 2, 3]] # [True, False, 25, 25.23, 'hello', True, [1, 2, 3]]
q = len(a)
print(q)

a += [1, 2, 3] # [True, False, 25, 25.23, 'hello', True, [1, 2, 3], 1, 2, 3]
print(a)
a = ['hi'] + a # ['hi', True, False, 25, 25.23, 'hello', True, [1, 2, 3], 1, 2, 3]
print(a)

q = [12, 54, 'hello', True, [1, 2, 3]]
w = q * 3 # [12, 54, 'hello', True, [1, 2, 3], 12, 54, 'hello', True, [1, 2, 3], 12, 54, 'hello', True, [1, 2, 3]]
print(w)

e = 54 in w # True
print(e)

q = [23, 56, -56, 78, 102, 458, 698]
w = max(q) #698
r = min(q) # -56
e = sum(q) # 1359
t = sorted(q) # [-56, 23, 56, 78, 102, 458, 698]
y = sorted(q, reverse=True) # [698, 458, 102, 78, 56, 23, -56]
print(y)

"""













