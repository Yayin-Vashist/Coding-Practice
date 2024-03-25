t = int(input())

while t:
    t -= 1

    n, k = [int(x) for x in input().split()]

    lst = [int(x) for x in input().split()]

    lst.sort()

    ind = 0
    cnt = 0
    for i in range(1, n):
        if lst[i] - lst[i - 1] > k:
            ind = i
        if i - ind > cnt:
            cnt = i - ind
    # if n == 1:
    #    print(0)
    # else:
    print(n - 1 - cnt)
