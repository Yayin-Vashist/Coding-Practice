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
    # op = 0
    for i in range(n-1):
        if lst[i]==1:
            lst[i]=2
            if lst[i-1]==2:
                lst[i] += 1
            # op +=1
        if lst[i+1]%lst[i]==0:
            lst[i+1]+=1
            # op += 1
            # if lst[i+1]%2 == 0:
            #         lst[i+1]+=1
                    # op += 1
    for i in lst:
        print(i, end = ' ')
    print()