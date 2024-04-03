import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = inp()

while t:
    t -= 1
    n = inp()
    lst = inlt()

    cnt = 0
    yes = True
    for i in range(len(lst)-2, -1, -1):
        if lst[i] >= lst[i+1]:
            while lst[i]>=lst[i+1]:
                lst[i] = lst[i] >> 1;
                cnt += 1
        if i != 0 and lst[i]==0:
            yes = False
            break
    if yes:
        print(cnt)
    else:
        print(-1)