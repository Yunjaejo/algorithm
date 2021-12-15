import sys



######## 메모리 초과 #########
# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())

# a = [[True] * n for _ in range(n)]
# b = []
#
# for i in range(n):
#     for j in range(n):
#         a[i][j] = (i + 1) * (j + 1)
#
# for nums in a:
#     b += nums
#
# b.sort()
#
# print(b[k])

# 메모리 초과가 난다. 케이스가 10^10까지 올라가는데 배열로 직접 뽑으려고 했기 때문.
# 이분탐색문제인데 이분탐색 방법으로 풀지도 않았다. 통과할 수 있게 꼭 다시 풀자
