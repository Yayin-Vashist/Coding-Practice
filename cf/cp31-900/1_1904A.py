t = int(input())

while t:
    t -= 1
    knight_a, knight_b = [int(x) for x in input().split()]
    king = [int(x) for x in input().split()]
    queen = [int(x) for x in input().split()]

    st = set()
    visited = set()
    i = 0
    j = 1

    piece_x, piece_y = king
    for j in range(8):
        if (piece_x + knight_a, piece_y + knight_b) not in st:
            st.add((piece_x + knight_a, piece_y + knight_b))
        # print(st, piece_x + knight_a, piece_y + knight_b)
        if knight_b > 0:
            knight_b = -knight_b
        elif knight_a > 0:
            knight_a = -knight_a
            knight_b = -knight_b
        else:
            knight_b, knight_a = -knight_a, -knight_b
    #    knight_a, knight_b = -knight_b, -knight_a
    # print(knight_a, knight_b)
    piece_x, piece_y = queen
    for j in range(8):
        if (piece_x + knight_a, piece_y + knight_b) in st:
            visited.add((piece_x + knight_a, piece_y + knight_b))
        #   print(visited, knight_a, knight_b)
        if knight_b > 0:
            knight_b = -knight_b
        elif knight_a > 0:
            knight_a = -knight_a
            knight_b = -knight_b
        else:
            knight_b, knight_a = -knight_a, -knight_b

    # print("set: ", st)
    # print("visited: ", visited)
    print(len(visited))
