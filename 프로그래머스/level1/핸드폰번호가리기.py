def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]
    # -- 번호 길이에서 뒷자리 4개를 뺸 개수만큼 *을 찍고 뒷자리 4개를 더한다.
