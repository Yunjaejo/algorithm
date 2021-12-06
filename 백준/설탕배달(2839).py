n = int(input())
bongji = 0

while n >= 0:
    if n % 5 == 0:
        bongji += (n // 5)
        print(bongji)
        break
    n -= 3
    bongji += 1
    if n < 0:
        print(-1)
        break
