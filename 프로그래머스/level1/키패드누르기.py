keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
          4: [0, 1], 5: [1, 1], 6: [2, 1],
          7: [0, 2], 8: [1, 2], 9: [2, 2],
          "*": [0, 3], 0: [1, 3], "#": [2, 3]}


def get_how_long(cur_num, next_num):
    Lcur, Rcur = keypad[cur_num]
    Lnext, Rnext = keypad[next_num]
    return abs(Lcur - Lnext) + abs(Rcur - Rnext)


def solution(numbers, hand):
    Lcur = '*'
    Rcur = '#'
    answer = ''

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            Lcur = num
        elif num in [3, 6, 9]:
            answer += 'R'
            Rcur = num
        else:
            how_many_move_L = get_how_long(Lcur, num)
            how_many_move_R = get_how_long(Rcur, num)
            if how_many_move_L > how_many_move_R:
                answer += 'R'
                Rcur = num
            elif how_many_move_L < how_many_move_R:
                answer += 'L'
                Lcur = num
            else:
                if hand == 'left':
                    answer += 'L'
                    Lcur = num
                else:
                    answer += 'R'
                    Rcur = num

    return answer
