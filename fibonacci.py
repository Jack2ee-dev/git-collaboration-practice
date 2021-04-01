def fibo_recur(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    if n == 2:
        return 1

    return fibo_recur(n-1) + fibo_recur(n-2)

n = int(input())
print(fibo_recur(n))

