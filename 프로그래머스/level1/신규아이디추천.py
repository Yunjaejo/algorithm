def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for w in new_id:
        if w.isalnum() or w in '-_.':
            answer += w
    while '..' in answer:
        answer = answer.replace('..', '.')
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        while True:
            answer += answer[-1]
            if len(answer) == 3:
                break
    return answer
