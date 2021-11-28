def hourglass_sum(arr):
    # Write your code here
    sum_hourglass = []
    z = 0
    next_row = 0
    next_row_counter = 3
    while z < 4:
        i = 0
        next_hourglass = 0
        counter = 3
        while i < 4:
            j = next_row
            lst_hr_glass = []
            j_plus_one = j + 1
            while j < next_row_counter:
                k = next_hourglass
                while k < counter:
                    if j == j_plus_one:
                        k += 1
                        lst_hr_glass.append(arr[j][k])
                        k += 1
                    else:
                        lst_hr_glass.append(arr[j][k])
                    k += 1
                j += 1
            sum_hourglass.append(lst_hr_glass)
            counter += 1
            next_hourglass += 1
            i += 1
        next_row += 1
        next_row_counter += 1
        z += 1
    max_sum = sum(sum_hourglass[0])
    for hr_glass in sum_hourglass:
        if sum(hr_glass) >= max_sum:
            max_sum = sum(hr_glass)
    print(max_sum)


hourglass_sum([[-1, -1, 0, -9, -2, -2],
               [-2, -1, -6, -8, -2, -5],
               [-1, -1, -1, -2, -3, -4],
               [-1, -9, -2, -4, -4, -5],
               [-7, -3, -3, -2, -9, -9],
               [-1, -3, -1, -2, -4, -5]])


