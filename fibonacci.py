def fibo_recur(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    if n == 2:
        return 1

    return fibo_recur(n-1) + fibo_recur(n-2)


def fibo_dp(n, dp=dict()):

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    if n in dp:
        return dp[n]

    dp[n] = fibo_dp(n-1, dp) + fibo_dp(n-2, dp)

    return dp[n]

a = int(input())
print(fibo_dp(a))
print(fibo_recur(a))

