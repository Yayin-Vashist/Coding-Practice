t = int(input())

while t:
    t -= 1

    a, b, c = [int(x) for x in input().split()]

    if c % 2 == 1:
        a += 1
    if a <= b:
        print("Second")
    else:
        print("First")
