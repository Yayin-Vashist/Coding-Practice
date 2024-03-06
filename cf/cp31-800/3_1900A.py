t = int(input())

while t:
    t -= 1
    n = int(input())
    lst = input()

    c, tc = False, 0
    for i in range(n):
        if lst[i] == ".":
            tc += 1
        if (
            i > 0
            and i < n - 1
            and lst[i] == "."
            and lst[i + 1] == "."
            and lst[i - 1] == "."
        ):
            c = True
            break
    if c:
        print(2)
    else:
        print(tc)
