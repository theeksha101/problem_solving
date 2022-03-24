def foo(x):
    if x == 0:
        return 1
    elif x % 2 == 0:
        return 2 * x * foo(x - 2)
    else:
        return (x -3) * x * foo(x + 1)


print(foo(4))