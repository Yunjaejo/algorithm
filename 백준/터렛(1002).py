case = int(input())
for _ in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    point_range = (abs(x1 - x2) * abs(x1 - x2) + abs(y1 - y2) * abs(y1 - y2)) ** 0.5
    if point_range == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 == point_range or abs(r1 - r2) == point_range:
        print(1)
    elif r1 + r2 > point_range > abs(r1 - r2):
        print(2)
    else:
        print(0)
