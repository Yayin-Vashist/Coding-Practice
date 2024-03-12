t = int(input())

while t:
    t -= 1

    n = int(input())
    lst = [int(x) for x in input().split()]

    o = 0
    if len(lst) < 2:
        print("NO")
    else:
        for i in lst:
            if i % 2 == 1:
                o += 1
        if o % 2 == 1:
            print("NO")
        else:
            print("YES")
