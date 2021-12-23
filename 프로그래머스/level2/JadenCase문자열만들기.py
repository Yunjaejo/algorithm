def solution(s):
    s = s.lower()
    word = s.split()
    for i in range(len(word)):
        word[i] = word[i][0].upper() + word[i][1:]

    answer = ' '.join(word)
    return answer
