n = int(input())
cnt = 0
origin = n


def sum_n(n):  # 두 자리 수의 각 자리의 합을 구하는 함수
    return sum(map(int, (list(str(n)))))  # 정수 -> 문자열 -> 배열 -> 정수의 배열 -> 합


def get_one(n):  # 일의자리의 수를 구하는 함수
    list_n = list(str(n))[-1:]  # 정수 -> 문자열 -> 배열 -> 마지막자리 찾기
    return int(list_n[0])  # 마지막 자리 수(문자)를 정수로 변경


while True:
    n = get_one(n) * 10 + get_one(sum_n(n))  # n의 일의자리 x 10 + 합의 일의자리
    cnt += 1  # 더하고 카운트 + 1
    if n == origin:  # 더한 값이 처음과 같다면 중지
        break

print(cnt)
