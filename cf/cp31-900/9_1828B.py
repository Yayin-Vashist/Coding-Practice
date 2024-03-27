import math
import sys

input = sys.stdin.readline


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


t = inp()

while t:
    t -= 1
    n = inp()

    lst = inlt()

    a = abs(-lst[0] + 1)

    for i, ele in enumerate(lst):
        a = math.gcd(a, abs(i - ele + 1))
    print(a)
