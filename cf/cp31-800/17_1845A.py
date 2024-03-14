t = int(input())

while t:
    t -= 1
    lst = []
    n, k, x = [int(x) for x in input().split()]
    if k == 1:
        print("NO")
    elif k == 2 and x == 1 and n % 2 == 1:
        print("NO")
    else:
        target = n
        while target > 0:
            if target >= k and x != k:
                target -= k
                lst.append(k)
            elif target >= k and x == k:
                target -= k - 1
                lst.append(k - 1)
            elif target != x:
                lst.append(target)
                target = 0
            else:
                if target - 1 > 0:
                    lst.append(target - 1)
                    lst.append(1)
                    target = 0
                else:
                    lst[len(lst) - 1] -= 1
                    lst.append(2)
                    target = 0
        print("YES")
        print(len(lst))
        for i in lst:
            print(i, end=" ")
        print()
