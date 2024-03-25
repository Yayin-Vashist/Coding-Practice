t = int(input())

while t:
    t -= 1
    n = int(input())

    cnt = 1
    for i in range(2, n + 1):
        if n % i != 0:
            break
        cnt += 1
    print(cnt)
