import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

nums_average_value = round(sum(nums) / n)


def get_center_value(array):
    array = sorted(array)
    return array[n // 2]


def get_mode(array):
    array = sorted(array)
    commons = Counter(array).most_common()
    if len(commons) > 1:
        if commons[0][1] == commons[1][1]:
            return commons[1][0]
        else:
            return commons[0][0]
    else:
        return commons[0][0]


def get_range(array):
    array = sorted(array)
    return array[-1] - array[0]


print(nums_average_value)
print(get_center_value(nums))
print(get_mode(nums))
print(get_range(nums))
