t = int(input())

while t:
    t -= 1

    n = int(input())
    lst = [int(x) for x in input().split()]

    cnt = 0
    maxi = 0

    for i in range(n):
        if lst[i] == 0:
            cnt += 1
            if cnt > maxi:
                maxi = cnt
            continue
        cnt = 0
    print(maxi)
