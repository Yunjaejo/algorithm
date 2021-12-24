def solution(s):
    answer = ''
    s = s.lower()
    word = s.split(' ')
    for w in word:
        w = w.capitalize()
        answer = answer + w + ' '
    return answer[:-1]
