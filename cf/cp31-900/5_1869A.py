t = int(input())

while t:
    t -= 1

    n = int(input())

    lst = [int(x) for x in input().split()]

    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n)
        print(1, n - 1)
        print(n - 1, n)
        print(n - 1, n)
