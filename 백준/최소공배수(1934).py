import sys

t = int(sys.stdin.readline())


def gcd(x, y):  # 유클리드 호제법으로 최대공약수 구하기, Greatest Common Divisor
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):  # 최소공배수 = (x * y) / 최대공약수, Least Common Multiple
    return (x * y) // gcd(x, y)


for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))


# 유클리드 호제법? O(logN)
# 2개의 자연수 x, y (x > y)를 받은 후, x % y 를 r이라 하면 a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 즉 b를 r로 나눈 나머지 r1을 구하고, 다시 r을 r1으로 나눈 나머지를 구하여 결국 rN이 0이 되었을 때 나누는 수가 x와 y의 최대공약수이다.

