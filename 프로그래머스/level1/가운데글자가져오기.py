def solution(s):
    answer = ''
    centerWord = len(s) // 2  # 자르는 글자 수
    if len(s) % 2 == 0:  # 짝수면
        answer = s[centerWord-1: centerWord+1]  # 중간 1칸 앞부터 중간 1칸 뒤까지
    else:  # 홀수면
        answer = s[centerWord]  # 글자의 중간만
    return answer