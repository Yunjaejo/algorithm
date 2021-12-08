import sys

n = int(sys.stdin.readline())


stack = []
for _ in range(n):
    method = sys.stdin.readline().strip().split()
    if len(method) == 1:
        if method[0] == 'pop':
            print(stack.pop()) if stack else print(-1)
        elif method[0] == 'size':
            print(len(stack))
        elif method[0] == 'empty':
            print(0) if stack else print(1)
        elif method[0] == 'top':
            print(stack[-1]) if stack else print(-1)
    elif len(method) == 2:
        stack.append(int(method[1]))

