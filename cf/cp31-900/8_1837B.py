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
    st = insr()
    s, f, c = 0, 0, 0

    for i in st:
        if i == "<":
            c += 1
            if c > f:
                f = c
        else:
            c -= 1
            if c < s:
                s = c
    print(f - s + 1)
