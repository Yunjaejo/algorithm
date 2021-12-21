import sys
sys.setrecursionlimit(10 ** 6)

memo = {
    0: 0,
    1: 1
}


def fibo(n, memo):
    if n in memo:
        return memo[n]
    else:
        next_value = fibo(n - 1, memo) + fibo(n - 2, memo)
        memo[n] = next_value
        return next_value


def solution(n):
    return fibo(n, memo) % 1234567
