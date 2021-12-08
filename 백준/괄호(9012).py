import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ps = sys.stdin.readline()
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

