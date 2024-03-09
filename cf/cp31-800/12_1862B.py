t = int(input())

while t:
    t -= 1
    num = int(input())
    lst = [int(x) for x in input().split()]
    new = [lst[0]]

    for i in range(1, num):
        if lst[i - 1] > lst[i]:
            new.append(lst[i])
        new.append(lst[i])
    print(len(new))
    for x in new:
        print(x, end=" ")
    print()
