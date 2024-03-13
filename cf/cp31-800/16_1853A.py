t = int(input())

while t:
    t -= 1

    n = int(input())

    lst = [int(x) for x in input().split()]

    if n < 2:
        print(0)
    else:
        min = lst[1] - lst[0]
        for i in range(2, len(lst)):
            if lst[i] - lst[i - 1] < min:
                min = lst[i] - lst[i - 1]
        if min < 0:
            print(0)
        else:
            print(min // 2 + 1)
