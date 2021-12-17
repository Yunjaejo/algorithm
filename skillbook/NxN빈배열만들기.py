import sys

# n x n 의 빈배열 만들기
n = int(sys.stdin.readline())
a = [[True] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = (i + 1) * (j + 1)


# 2차원배열 1차원으로 뽑기
b = []

for nums in a:
    b += nums

