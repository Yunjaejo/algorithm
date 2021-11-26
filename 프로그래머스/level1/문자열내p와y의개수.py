def solution(s):
    s = s.lower()  # 문자열 s를 소문자로 변환
    return s.count('p') == s.count('y')  # 문자열에서 p의 개수가 y의 개수와 같다면 True, 아니면 False 리턴
