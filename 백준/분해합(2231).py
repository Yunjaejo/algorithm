import sys


def get_bhh(x):  # 정수 x의 분해합을 구하는 함수, 분해합은 자기자신 + 각 자리수의 합
    num_list = map(int, list(str(x)))
    return x + sum(num_list)


n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n+1):
    if n == get_bhh(i):
        cnt = i
        break

print(cnt)

