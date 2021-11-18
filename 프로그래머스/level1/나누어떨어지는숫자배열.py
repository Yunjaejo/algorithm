def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:  # --- 나누어 떨어진다면 정답배열에 추가
            answer.append(i)
            answer.sort()
    if len(answer) == 0:  # --- 정답배열에 하나도 없다면 -1을 리턴
        answer.append(-1)

    return answer
