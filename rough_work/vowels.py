def print_next_vovel_string(st):
    lower = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    upper = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    arr = ['a', 'e', 'i', 'o', 'u']

    N = len(st)

    for i in range(N):

        c = st[i]

        if c == c.lower():
            if (c == 'a' or c == 'e' or
                    c == 'i' or c == 'o' or
                    c == 'u'):
                index = lower[st[i]] + 1
                newindex = index % 5
                st = st.replace(st[i], arr[newindex], 1)
        else:
            if (c == 'A' or c == 'E' or
                    c == 'I' or c == 'O' or
                    c == 'U'):
                index = upper[st[i]] + 1
                newindex = index % 5
                st = st.replace(st[i], arr[newindex].upper(), 1)


    return st


# Driver function
if __name__ == "__main__":
    st = "gEeksforgeeks"
    print(print_next_vovel_string(st))

# This code is contributed by Chitranayal
