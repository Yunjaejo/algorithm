import sys

t = int(sys.stdin.readline())

memo = {
    0: 0,
    1: 1,
}


def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    else:
        next_value = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = next_value
        return next_value


for _ in range(t):
    case = int(sys.stdin.readline())
    if case == 0:
        print('1 0')
    else:
        print(fibonacci(case - 1, memo), fibonacci(case, memo))  # n 번째에서 0의 개수는 n-1과 같다.
