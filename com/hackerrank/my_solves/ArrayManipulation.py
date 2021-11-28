def arrayManipulation(n, queries):
    # Write your code here

    result_array = [0] * n
    i = 0
    
    # result_array = [0 for i in range(n)]
    # print(result_array)
    # max_result = 0
    # for query in queries:
    #     for i in range((query[0] - 1), (query[1])):
    #         result_array[i] = (result_array[i] + query[2])
    #         if max_result < result_array[i]:
    #             max_result = result_array[i]
    #     print(result_array)
    # return max_result


queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
n = 10
print(arrayManipulation(n, queries))
