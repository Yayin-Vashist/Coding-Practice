t = int(input())

while t:
    t -= 1
    n, x = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]

    maxi = lst[0]
    for i in range(1, n):
        maxi = max(maxi, lst[i] - lst[i - 1])
    maxi = max(maxi, 2 * (x - lst[n - 1]))
    print(maxi)
