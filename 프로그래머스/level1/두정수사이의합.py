def solution(a, b):
    if a < b:
        return sum(list(range(a, b + 1)))  # a부터 b 까지의 정수를 리스트화시켜서 더함
    else:
        return sum(list(range(b, a + 1)))  # b부터 a 까지의 정수를 리스트화시켜서 더함
