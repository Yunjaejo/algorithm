def solution(x):
    xToArr = map(int, list(str(x)))  # --- 인자 x를 리스트로 바꾸기 위해 문자열로 타입변경 후 리스트화시킨 뒤 각 항을 숫자로 다시 변경,
    sumX = sum(xToArr)  # --- 각 항이 숫자이니 모두 더한다.
    return True if x % sumX == 0 else False  # --- 파이썬의 삼항연산자. x % sumX === 0 ? true : false 와 같다
