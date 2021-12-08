import sys

k = int(sys.stdin.readline())
answer = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
        answer.append(n)
    else:
        answer.pop()

print(sum(answer))
