t = int(input())

lst = [int(x) for x in input().split()]
min = abs(lst[0])
for i in range(1, t):
    if abs(lst[i]) < min:
        min = abs(lst[i])
print(min)
