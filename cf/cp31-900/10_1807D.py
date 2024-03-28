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

t = int(input())

while t:
    t -= 1

    n, q = invr()
    lst = inlt()
    queries = list()
    for i in range(q):
        queries.append(inlt())
    lst1 = list()
    c = 0
    for i in lst:
        if i%2==0:
            c += 1
        lst1.append(c)
    odd = True
    if (n-c)%2==0:
        odd =False
    # print(f"{n},,,,,,,{c}-------{odd}")
    # print(f"-----> {lst1}")
    for i in queries:
        l, r, k = i
        if l==1:
            c = lst1[r-1]
        else:
            c =lst1[r-1] - lst1[l-2]
        ans = odd
        if k%2==0 and (l-r+1-c)%2==1:
            ans = not odd
        elif k%2==1 and c%2==1:
            ans = not odd
        if ans:
            print("YES")
        else:
            print("NO")