def solution(s):
    s = ''.join(sorted(s, reverse=True))  # 문자열은 sort 안되지만 sorted 로 넣어주는건 됨. reverse=True 는 내림차순 정렬.
    return s
