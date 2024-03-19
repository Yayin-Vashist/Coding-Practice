t = int(input())

while t:
    t -= 1
    n, k = [int(x) for x in input().split()]
    if n % 2 == 0:
        print("YES")
    elif k % 2 == 1 and n >= k:
        print("YES")
    else:
        print("NO")
