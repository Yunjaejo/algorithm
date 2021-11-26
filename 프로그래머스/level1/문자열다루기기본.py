def solution(s):
    try:
        if (len(s) == 4 or len(s) == 6) and int(s):  # 문자열 s의 길이가 4거나 6이면서, 정수로 변환이 된다면?
            return True
        else:
            return False
    except:  # int(s) 과정에서 에러가 난다면, 즉 문자열 s가 숫자로만 이뤄진게 아닐 때
        return False
