t =  int(input())

while t:
    t -=  1

    n, k, x =[int(x) for x in input().split()]

    if x >= k*(k+1)/2 and x <= (2*n - k + 1)*k/2:
        print("YES")
    else:
        print("NO")
