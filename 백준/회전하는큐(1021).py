import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
array = map(int, sys.stdin.readline().split())

queue = deque([])
cnt = 0  # 몇번만에 되는지를 담을 변수

for num in range(n):
    queue.append(num + 1)  # 1부터 n까지 queue 배열에 담는다

for x in array:  # 내가 뽑고싶은 수배열의 요소를 다 돌기
    i = queue.index(x)  # 그 수가 queue 배열에서의 몇번째 인덱스인지
    if i == 0:  # 0번째 인덱스라면(제일 앞에 있다면)
        queue.popleft()  # 바로 뽑아버린다.
    else:  # 0번째 인덱스가 아니라면
        if i < (len(queue) - i):  # 왼쪽으로 돌지, 오른쪽으로 돌지 계산한다.
            cnt += i
            queue.rotate(-i)
            queue.popleft()
        else:
            cnt += (len(queue) - i)
            queue.rotate(len(queue) - i)
            queue.popleft()

print(cnt)
