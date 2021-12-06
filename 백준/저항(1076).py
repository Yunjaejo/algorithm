value = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']  # 배열의 인덱스가 문제에서의 값과 같음.

no1, no2, no3 = value.index(input()), value.index(input()), value.index(input())

print((no1 * 10 + no2) * (10 ** no3))