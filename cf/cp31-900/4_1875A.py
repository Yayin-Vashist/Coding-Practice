t = int(input())

while t:
    t -= 1

    a, b, n = [int(x) for x in input().split()]
    cnt = b
    lst = [int(x) for x in input().split()]

    for i in lst:
        if i >= a-1:
            cnt += a-1
        else:
            cnt += i
    print(cnt)
