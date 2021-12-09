import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

stack = deque([])
answer = []

for i in range(n):
    stack.append(i + 1)

while True:
    stack.rotate(-k + 1)
    answer.append(str(stack.popleft()))
    if len(stack) == 0:
        break

# print('<', end='')
# for i in range(len(answer)):
#     if i == len(answer) - 1:
#         print(answer[i], end='')
#     else:
#         print(answer[i], end=', ')
# print('>')

print('<' + ', '.join(answer) + '>')
