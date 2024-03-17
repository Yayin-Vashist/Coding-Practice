t = int(input())

while t:
    t -= 1
    n = int(input())

    lst = [int(x) for x in input().split()]

    for i in lst:
        print(n - i + 1, end=" ")
    print()
