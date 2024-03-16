t = int(input())

while t:
    t -= 1
    n = int(input())

    lst = [int(x) for x in input().split()]

    c = 0

    for i in lst:
        if i == -1:
            c += 1
    if c <= n // 2:
        if c % 2 == 1:
            print(1)
        else:
            print(0)
    else:
        if n // 2 % 2 == 1:
            print((c - n // 2) + 1)
        else:
            print(c - n // 2)
