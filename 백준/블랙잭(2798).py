import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

maximum = 0

card_combinations = list(combinations(cards, 3))  # cards 배열의 3개의 요소를 조합하여 나올 수 있는 모든 케이스를 튜플배열로 변환

for cards in card_combinations:  # 카드 3개 조합으로 나오는 배열을 반복
    sum_card = sum(cards)
    if maximum < sum_card <= m:  # 여태까지의 최대보다 크면서 입력받은 최대값을 넘지 않을 때 maximum 갱신
        maximum = sum_card

print(maximum)
