def array_2d(arr):
    # want to find the maximum hourglass sum
    # minimum hourglass sum = -9 * 7 = -63
    max_sum = -63

    for i in range(4):
        for j in range(4):

            # sum of top 3 elements
            top = sum(arr[i][j:j + 3])

            # sum of the mid element
            mid = arr[i + 1][j + 1]

            # sum of bottom 3 elements
            bottom = sum(arr[i + 2][j:j + 3])

            hourglass = top + mid + bottom

            if hourglass > max_sum:
                max_sum = hourglass

    return max_sum


print(array_2d([[-1, -1, 0, -9, -2, -2],
                [-2, -1, -6, -8, -2, -5],
                [-1, -1, -1, -2, -3, -4],
                [-1, -9, -2, -4, -4, -5],
                [-7, -3, -3, -2, -9, -9],
                [-1, -3, -1, -2, -4, -5]]))
