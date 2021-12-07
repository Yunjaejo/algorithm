def how_many_prime(m, n):
    cnt = 0
    n = n + 1
    prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
    for i in range(m + 1, n):
        if i > 1 and prime[i]:
            cnt += 1
    print(cnt)


while True:
    n = int(input())
    if n == 0:
        break
    how_many_prime(n, 2 * n)
