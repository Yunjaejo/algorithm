import sys

n = int(sys.stdin.readline())
nums = []
num = 666

while True:
    if '666' in str(num):
        nums.append(num)
    num += 1
    if len(nums) == n:
        break

print(nums[-1])
