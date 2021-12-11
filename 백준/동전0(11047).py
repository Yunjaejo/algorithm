import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0  # 한 동전당 몇번 쓰이는지
total_cnt = 0  # cnt 들을 모두 더할 변수
coin = []  # 동전의 종류를 담을 배열

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):  # coin[-1] 부터 coin[0] 까지 역순으로 더해야 최소값이 나옴
    if k >= coin[i]:
        cnt = k // coin[i]
        k = k - (coin[i] * cnt)
        total_cnt += cnt

print(total_cnt)

