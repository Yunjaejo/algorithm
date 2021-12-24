def solution(s):
    boom = []
    cnt = 0
    s = list(s)
    for w in s:
        boom.append(w)
        if len(boom) >= 2 and boom[-1] == boom[-2]:
            boom.pop()
            boom.pop()
            cnt += 1
    if len(boom):
        return 1
    else:
        return 0
