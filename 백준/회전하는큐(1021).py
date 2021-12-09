import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
array = map(int, sys.stdin.readline().split())

queue = deque([])
cnt = 0

for num in range(n):
    queue.append(num + 1)

for x in array:
    i = queue.index(x)
    if i == 0:
        queue.popleft()
    else:
        if i < (len(queue) - i):
            cnt += i
            queue.rotate(-i)
            queue.popleft()
        else:
            cnt += (len(queue) - i)
            queue.rotate(len(queue) - i)
            queue.popleft()

print(cnt)
