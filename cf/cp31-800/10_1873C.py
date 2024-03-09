t = int(input())

while t:
    t -= 1
    lst = []
    for i in range(10):
        a = input()
        lst.append(a)
    points = 0
    ringi, ringj = None, None
    for i in range(10):
        for j in range(10):
            if lst[i][j] == "X":
                if i < 5:
                    ringi = i
                else:
                    ringi = 9 - i
                if j < 5:
                    ringj = j
                else:
                    ringj = 9 - j
                if ringi == 0 or ringj == 0:
                    points += 1
                elif ringi == 1 or ringj == 1:
                    points += 2
                elif ringi == 2 or ringj == 2:
                    points += 3
                elif ringi == 3 or ringj == 3:
                    points += 4
                elif ringi == 4 or ringj == 4:
                    points += 5
    print(points)
