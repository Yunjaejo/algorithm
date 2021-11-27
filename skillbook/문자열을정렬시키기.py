def solution(s):
    s = ''.join(sorted(s, reverse=True))  # 문자열은 sort 안되지만 sorted 로 넣어주는건 됨. reverse=True 는 내림차순 정렬.
    return s

a = 'aedcb'
a.sort()  # 에러가 난다. str 데이터 타입에는 sort() 메서드가 없음.
a = ''.join(sorted(a))  # 에러 안남. sorted 는 가능해서 정렬한 문자열을 빈문자열에 추가하는 식으로 대입.
