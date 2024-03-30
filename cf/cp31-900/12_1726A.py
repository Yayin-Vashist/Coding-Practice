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

    diff = lst[n - 1] - lst[0]
    low = lst[n - 1]
    high = lst[n - 1]
    for i in range(n - 1):
        if -lst[i + 1] + lst[i] > diff:
            diff = -lst[i + 1] + lst[i]
        if lst[i] < low:
            low = lst[i]
        if lst[i] > high:
            high = lst[i]
    if high - lst[0] > diff:
        diff = high - lst[0]
    if lst[n - 1] - low > diff:
        diff = lst[n - 1] - low
    print(diff)
