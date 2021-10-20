def print_board(bo: list, offset=0):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(' ' * offset, end='')
            print("- - - - - - - - - - - - ")

        print(' ' * offset, end='')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

    print(' ' * offset, '_'*21)
