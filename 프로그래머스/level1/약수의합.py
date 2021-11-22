def solution(n):
    divide = []
    for i in range(n):
        if n % (i + 1) == 0:  # -- 나누어 떨어지는것만, 즉 약수만 걸리면
            divide.append(i + 1)  # -- 그 수를 정답배열에 추가
    return sum(divide)
