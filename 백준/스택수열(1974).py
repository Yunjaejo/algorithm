import sys

n = int(sys.stdin.readline())

stack = []
answer = []
cnt = 1
is_true = True

for _ in range(n):
    num = int(sys.stdin.readline())

    while num >= cnt:
        answer.append('+')
        stack.append(cnt)
        cnt += 1

    if stack[-1] == num:
        answer.append('-')
        stack.pop()
    else:
        is_true = False


if is_true:
    for ans in answer:
        print(ans)
else:
    print('NO')
