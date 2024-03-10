t = int(input())

while t:
    t -= 1
    n = int(input())
    lst = [int(x) for x in input().split()]
    b = []
    c = []
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    for i in lst:
        if i == maxi:
            c.append(i)
        else:
            b.append(i)
    if len(b) == 0:
        print(-1)
    else:
        print(len(b), len(c))
        for i in b:
            print(i, end=" ")
        print()
        for i in c:
            print(i, end=" ")
