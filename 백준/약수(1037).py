import sys

how_many = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

print(a[0] * a[-1])