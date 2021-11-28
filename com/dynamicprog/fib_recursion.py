# Function for nth Fibonacci number

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        result = Fibonacci(n - 1) + Fibonacci(n - 2)
        return result


# Driver Program

print(Fibonacci(9))
