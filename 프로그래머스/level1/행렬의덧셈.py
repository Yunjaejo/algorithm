def solution(arr1, arr2):
    answer = []  # 정답배열
    for i in range(len(arr1)):
        answer_index = []  # 정답배열에 들어가는 인덱스배열
        for j in range(len(arr1[0])):
            answer_index.append(arr1[i][j] + arr2[i][j])  # 인덱스배열에 값들을 집어넣는다.
        answer.append(answer_index)
    return answer
