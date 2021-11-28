# fibonacci of Nth number using dynamic programming

def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


memo = {}
print(fib(9, memo))
