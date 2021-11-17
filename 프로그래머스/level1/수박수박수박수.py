def solution(n):
    if n == 1 :
        return '수'
    elif n % 2 == 0:
        answer = '수박' * int(n/2)
        return answer
    elif n % 2 == 1:
        return '수' + ('박수' * int(n//2))