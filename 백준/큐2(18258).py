import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n):
    method = sys.stdin.readline().strip().split()
    if len(method) == 1:
        if method[0] == 'front':
            print(queue[0]) if queue else print(-1)
        if method[0] == 'back':
            print(queue[-1]) if queue else print(-1)
        if method[0] == 'pop':
            print(queue.popleft()) if queue else print(-1)
        if method[0] == 'size':
            print(len(queue))
        if method[0] == 'empty':
            print(1) if len(queue) == 0 else print(0)
    elif len(method) == 2:
        queue.append(int(method[1]))
