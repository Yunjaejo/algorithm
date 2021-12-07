n = int(input())
cnt = 0
origin = n


def sum_n(n):
    return sum(map(int, (list(str(n)))))


def get_one(n):
    list_n = list(str(n))[-1:]
    return int(list_n[0])


while True:
    n = get_one(n) * 10 + get_one(sum_n(n))
    cnt += 1
    if n == origin:
        break

print(cnt)
