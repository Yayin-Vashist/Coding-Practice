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

    start = False
    cnt = 0
    for i in lst:
        if i != 0 and not start:
            start = True
            cnt += 1
        elif i == 0 and start:
            start = False
    print(min(cnt, 2))
