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
    mini = n // 6 + 1
    if n % 6 == 0:
        mini -= 1
    maxi = n // 4
    if n % 2 == 1 or n < 4:
        print(-1)
    else:
        print(mini, maxi)
