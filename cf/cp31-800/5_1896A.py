t = int(input())

while t:
    t -= 1
    n = int(input())
    lst = [int(x) for x in input().split()]
    if lst[0] == 1:
        print("YES")
    else:
        print("NO")
