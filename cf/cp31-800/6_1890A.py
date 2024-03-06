t = int(input())

while t:
    t -= 1
    n = int(input())
    lst = [int(x) for x in input().split()]
    freq = {}
    c = 0
    arr = []
    for i in lst:
        if i not in freq:
            freq[i] = 1
            c += 1
            arr.append(i)
        elif i in freq:
            freq[i] += 1
        if c > 2:
            break
    if c == 1:
        print("YES")
    elif c > 2:
        print("NO")
    else:
        if freq[arr[0]] == n // 2 or freq[arr[1]] == n // 2:
            print("YES")
        else:
            print("NO")
