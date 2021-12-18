def solution(n):
    n = list(str(n))  # 정수 -> 문자열 -> 배열
    n.sort(reverse=True)  # 배열 거꾸로 정렬

    return int("".join(n))  # join 사용하여 일반문으로 뽑고 정수로 형변환
