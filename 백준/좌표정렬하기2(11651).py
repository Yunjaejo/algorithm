import sys

n = int(sys.stdin.readline())
xy = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy.append([x, y])

aa = sorted(xy, key=lambda x: (x[1], x[0]))

for x, y in aa:
    print(x, y)
