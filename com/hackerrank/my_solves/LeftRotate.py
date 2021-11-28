def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        popped_number = arr.pop(0)
        arr.append(popped_number)
    print(arr)


rotateLeft(4, [1, 2, 3, 4, 5])