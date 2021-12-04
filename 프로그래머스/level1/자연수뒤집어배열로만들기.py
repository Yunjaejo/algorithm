def solution(n):
    n = list(str(n))  # 자연수를 문자열로 바꾼 뒤 리스트화 시킴
    n.reverse()  # 리스트를 뒤집음
    return list(map(int, n))  # 뒤집은 리스트를 숫자배열로 바꿈
