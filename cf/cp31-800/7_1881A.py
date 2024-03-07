t = int(input())

while t:
    t -= 1
    n, m = [int(x) for x in input().split()]
    x = input()
    s = input()

    count = 0
    while len(x) < len(s):
        x += x
        count += 1
    if s in x:
        print(count)
    else:
        x += x
        count += 1
        if s in x:
            print(count)
        else:
            print(-1)
