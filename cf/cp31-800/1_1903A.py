ni = int(input())

while ni:
    ni -= 1
    n, k = [int(x) for x in input().split()]
    lst = input().split()
    lst = [int(x) for x in lst]
    yes = True
    if k == 1:
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                # print(lst, end="\n\n")
                # print("hey i = ", i, " lst[i] = ", lst[i], " lst[i+1] = ", lst[i + 1])
                yes = False
                break
    # for i in range(n):
    #     print("lst[i] = ", lst[i])
    # print(lst)
    if yes:
        print("YES")
    else:
        print("NO")
#    print(lst)
