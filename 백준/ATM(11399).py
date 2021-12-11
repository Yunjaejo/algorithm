import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

cur_time = 0
total_time = []
p.sort()

for i in range(n):
    cur_time += p[i]
    total_time.append(cur_time)

print(sum(total_time))
