import sys

t = int(sys.stdin.readline())


memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2
}


def pado(n, memo):
    if n in memo:
        return memo[n]
    else:
        next_value = pado(n - 2, memo) + pado(n - 3, memo)
        memo[n] = next_value
        return next_value


for _ in range(t):
    case = int(sys.stdin.readline())
    print(pado(case, memo))
