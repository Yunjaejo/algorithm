import sys
solution = sys.stdin.readline().rstrip().split('-')
array = []
answer = 0


def sum_all_plus(nums):  # solution 이 ['3', '3+5', '7', '7+2'] 이렇게 나오는데 모두 정수로 바꾸고 '+'식을 계산해주는 함수
    nums = nums.split('+')
    if len(nums) > 1:
        result = 0
        for item in nums:
            result += int(item)
        return result
    else:
        return int(nums[0])


for i in solution:  # 인자들에게 라인7에서 만든 함수를 먹여서 정답배열에 추가한다
    i = sum_all_plus(i)
    array.append(i)

for i in range(len(array)):  # 정답배열의 첫번째 인덱스만 더하고, 나머지는 모두 뺀다.
    if i == 0:
        answer += array[i]
    else:
        answer -= array[i]

print(solution)
print(answer)
