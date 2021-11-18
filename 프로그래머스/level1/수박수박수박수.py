def solution(n):
    if n % 2 == 0:  # --- n이 짝수라면
        answer = '수박' * int(n/2)  # --- 수박이라는 두글자에 n의 절반만큼 곱해서 출력
    else:  # --- n이 홀수라면
        answer = '수' + ('박수' * (n//2))  # --- 수 라는 글자에 박수를 n의 절반으로 나눈 몫만큼 반복해서 더함.

    return answer