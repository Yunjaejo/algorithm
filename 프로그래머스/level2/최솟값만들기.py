def solution(A,B):
    answer = []
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer.append(A[i] * B[i])
    return sum(answer)
