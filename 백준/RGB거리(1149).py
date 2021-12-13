import sys

n = int(sys.stdin.readline())

houses = []

for _ in range(n):  # 0 1 2
    r, g, b = map(int, sys.stdin.readline().split())
    houses.append([r, g, b])

for i in range(1, n):  # 1 2
    houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])  # R
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])  # G
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])  # B

print(min(houses[-1]))
