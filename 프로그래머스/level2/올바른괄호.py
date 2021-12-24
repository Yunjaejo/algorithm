def solution(s):
    arr = []
    for w in s:
        if w == '(':
            arr.append(w)
        elif arr and w == ')':
            arr.pop()
        else:
            return False
    if len(arr) == 0:
        return True
    else:
        return False
