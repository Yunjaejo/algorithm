# m 부터 n 까지의 소수를 구하는 로직
def get_prime(m, n):
    n = n + 1  # n 까지 세야하니까
    prime = [True] * n  # n개의 True 배열 생성
    for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근 까지만 검사
        if prime[i]:  # prime의 i번째가 트루라면
            for j in range(i * i, n, i):  # i의 배수들을 False 로 변환
                prime[j] = False
    for i in range(m, n):
        if i > 1 and prime[i]:  # 1 이상이면서 남은 소수들
            print(i)

# m 부터 n 까지의 소수의 개수를 구하는 로직
def how_many_prime(m, n):
    cnt = 0
    n = n + 1
    prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False
    for i in range(m, n):
        if i > 1 and prime[i]:
            cnt += 1
    print(cnt)

