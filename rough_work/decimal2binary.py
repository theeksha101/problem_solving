def to_binary(num: int):
    divider = num
    remainder = []
    while divider >= 1:
        remainder.append(int(divider % 2))
        divider = int(divider / 2)
    return remainder


print(to_binary(11))
