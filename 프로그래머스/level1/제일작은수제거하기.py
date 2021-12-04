def solution(arr):
    arr.remove(min(arr))  # 배열의 가장 작은 수를 지움
    if len(arr) == 0:  # 지운 뒤 하나도 남아있지 않다면
        return [-1]  # [-1] 리턴
    return arr  # 아니면 지운거 리턴
