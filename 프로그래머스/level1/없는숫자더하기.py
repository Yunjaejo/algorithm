def solution(numbers):
    totalNumbers = [0,1,2,3,4,5,6,7,8,9]  # -- 0~9 까지의 배열
    isNotExist = [x for x in totalNumbers if x not in numbers]  # -- 0~9까지의 배열 - numbers
    return sum(isNotExist)  # -- 남은 배열의 합
