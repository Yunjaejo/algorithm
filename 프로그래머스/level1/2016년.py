def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = day[(sum(month[0: a]) + b) % 7]
    if a < 1 | a > 12 | b < 1:
        return False
    elif (a % 2 == 0) & (b > 30):
        return False
    elif (a == 2) & (b > 29):
        return False

    return today