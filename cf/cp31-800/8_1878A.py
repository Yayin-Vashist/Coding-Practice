t = int(input())

while t:
    t -= 1
    n, k = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    if k in lst:
        print("YES")
    else:
        print("NO")
