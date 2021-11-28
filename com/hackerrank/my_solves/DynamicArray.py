#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamic_array(n, queries):
    # Write your code here
    last_answer = 0
    arr = []
    answer_array = []

    for i in range(n):
        arr.append([])
    for query in queries:
        if query[0] == 1:
            idx = ((query[1] ^ last_answer) % n)
            arr[idx].append(query[2])
        else:
            idx = ((query[1] ^ last_answer) % n)
            last_answer = arr[idx][query[2] % len(arr[idx])]
            answer_array.append(last_answer)
    return answer_array


if __name__ == '__main__':
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    print(dynamic_array(2, queries))
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # q = int(first_multiple_input[1])
    #
    # queries = []
    #
    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))
    #
    # print(dynamic_array(n, queries))
