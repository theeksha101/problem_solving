a = [2, 4, 5, 7, 8, 9]
sum = 0
for i in range(len(a) - 1):
    if a[i] % 2 == 0:
        sum = sum + a[i]

print(sum)
