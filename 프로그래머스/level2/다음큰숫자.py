def solution(n):
    cnt = n
    count1 = bin(n).count('1')
    while True:
        cnt += 1
        if bin(cnt).count('1') == count1:
            return cnt
