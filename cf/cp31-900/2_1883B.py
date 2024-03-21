t = int(input())

while t:
    t -= 1

    n, k = [int(x) for x in input().split()]

    s = input()

    dic = {}

    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    odd = 0
    for i in dic:
        if dic[i] % 2 == 1:
            odd += 1

    if odd-1 <= k:
        print("YES")
    else:
        print("NO")
