def solution(x, n):
    answer = []
    for i in range(n):  # n의 개수만큼 i로 돌기 0,1,2,3,4
        value = x + (x * i)  # answer 뽑는 수식
        answer.append(value)  # 리스트에 값 붙이기
    return answer