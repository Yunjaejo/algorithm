import math

how_many_case = int(input())

for _ in range(how_many_case):
    H, W, N = map(int, input().split())
    floor = N % H if N % H > 0 else H
    room = math.ceil(N / H)
    print(floor * 100 + room)
