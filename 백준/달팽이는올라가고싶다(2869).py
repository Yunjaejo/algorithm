A, B, V = map(int, input().split())

day = (V - B) / (A - B)

if day % 1 > 0:
    print(int(day) + 1)
else:
    print(int(day))


