n = int(input())

while n:
    n -= 1
    k = int(input())
    s = input()

    lex = True
    l = len(s)
    for i in range(l // 2):
        if ord(s[i]) > ord(s[l - 1 - i]):
            lex = False
            break
        if ord(s[i]) < ord(s[l - 1 - i]):
            break
    if k % 2 == 0 and lex:
        print(s)
    elif k % 2 == 1 and not lex:
        print(s[::-1])
    elif k % 2 == 0 and not lex:
        print(s[::-1], s, sep="")
    elif k % 2 == 1 and lex:
        print(s, s[::-1], sep="")
    # print(lex)
