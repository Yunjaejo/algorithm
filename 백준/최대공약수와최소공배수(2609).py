import sys

a, b = map(int, sys.stdin.readline().split())


def gcd(x, y):  # 유클리드 호제법으로 최대공약수 구하기, Greatest Common Divisor
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):  # 최소공배수 = (x * y) / 최대공약수, Least Common Multiple
    return (x * y) // gcd(x, y)


print(gcd(a, b))
print(lcm(a, b))
