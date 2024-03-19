t = int(input())

while t:
    t -= 1
    knight = [int(x) for x in input().split()]
    king = [int(x) for x in input().split()]
    queen = [int(x) for x in input().split()]

    st = set()

    i = 0
    j = 1

    for i, j in [king, queen]:
        for x in knight:
            set.add((i - x, j - y))
    print(st)
