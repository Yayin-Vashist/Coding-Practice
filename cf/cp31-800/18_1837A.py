t = int(input())

while t:
    t -= 1
    x, k = [int(x) for x in input().split()]
    if x % k == 0:
        print(2)
        print(x - 1, 1)
    else:
        print(1, x, sep="\n")
