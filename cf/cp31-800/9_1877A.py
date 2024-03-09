t = int(input())

while t:
    t -= 1
    n = int(input())
    lst = [int(x) for x in input().split()]
    sum = 0
    for i in lst:
        sum += i
    print(-sum)
