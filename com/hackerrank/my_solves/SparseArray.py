def matchingStrings(strings, queries):
    # Write your code here
    array_result = []
    for query in queries:
        result = 0
        for string in strings:
            if query == string:
                result += 1
        array_result.append(result)

    print(array_result)


strings = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
queries = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]
matchingStrings(strings, queries)