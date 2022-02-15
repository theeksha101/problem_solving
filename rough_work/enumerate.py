grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(enumerateGrocery)
print(type(enumerateGrocery))


for i in enumerate(grocery, 10):
    print(i)

# converting to list
print(tuple(enumerateGrocery))
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

letters = [('a', 'A'), ('b', 'B')]
for i, (lowercase, uppercase) in enumerate(letters):
    print("Letter #%d is %s/%s" % (i, lowercase, uppercase))

sym_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = "MCMXCIV"

# print("s[:-1]", s[:-1])
# print("s[::-1]", s[::-1])
# print("s[:-1][::-1]", s[:-1][::-1])
#
# for i, sym in enumerate(s[:-1][::-1]):
#     print(i, sym)

for i in s[:-1][::-1]:
    print(i)
