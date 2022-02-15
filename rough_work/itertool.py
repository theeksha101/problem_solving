from itertools import product


a = 'abs'
b = 'dsf'
c = 'dsc'

values = ['abs', 'def', 'dsc']

print(list(product(*values)))
print(list(product(values)))
print(list(product(*a)))
print(list(product(a)))
print(list(product(a, b, c)))
