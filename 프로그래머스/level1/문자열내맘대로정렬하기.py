def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))  # 문자열 strings를 정렬하는데 sort의 옵션으로 key값을 정한다. x의 n번째 인덱스로 먼저 정렬 후 나머지를 다시 정렬
    return strings
