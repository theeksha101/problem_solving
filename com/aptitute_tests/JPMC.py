#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'closestNumbers' function below.
#
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def closestNumbers(numbers):
    # Write your code here
    pos_nums = [abs(i) for i in numbers]
    list_diff = []
    pairs_diff = []
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(1, len_numbers):
            list_diff.append(abs(numbers[i]) - abs(numbers[j]))
            pairs_diff.append([numbers[i], numbers[j]])
    min_diff = min(list_diff)
    pairs_diff.sort()
    for i in range(len(pairs_diff)):
        if abs(pairs_diff[i][0]) - abs(pairs_diff[i][1]) == min_diff:
            pairs_diff[i].sort()
            print(pairs_diff[i][0], pairs_diff[i][1])


if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    closestNumbers(numbers)
