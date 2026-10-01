def recursion_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return recursion_fibonacci(n - 1) + recursion_fibonacci(n - 2)

def fibonacci_memo(n, memo=None):
    if n < 0:
        raise ValueError("n must be non-negative")

    if memo is None:
        memo = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]



def tabulation_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0

    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]



def fibonacci_optimized(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1

    return prev1

print(recursion_fibonacci(6)) 
print(fibonacci_memo(6))  # 8
print(tabulation_fibonacci(6))
print(fibonacci_optimized(6))