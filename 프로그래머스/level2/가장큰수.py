# from itertools import permutations
#
#
# def solution(numbers):
#     result = ''
#     answer = 0
#     numbers = list(map(str, numbers))
#     all_cases = list(permutations(numbers, len(numbers)))
#     for case in all_cases:
#         result = int(''.join(case))
#         if result > answer:
#             answer = result
#     return str(answer)

# ---------------시간 초과-----------------------

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)  # https://esoongan.tistory.com/103
    answer = ''.join(numbers)
    return answer if int(answer) != 0 else '0'  # numbers = [0, 0, 0, 0, 0] 일 때의 엣지케이스 고려
