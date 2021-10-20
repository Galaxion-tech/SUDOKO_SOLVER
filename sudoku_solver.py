from copy import deepcopy
from print_board import print_board
from utils import sq_list, x_list, y_list, break_loop
from sudo import sudo
# j= 0,1,2,3,4,5,6,7,8

def sudo_solver():  # main function
    global sudo
    for repetition in range(0, 10):  # repeating for 10 times
        for i in range(0, 9):
            for j in range(0, 9):
                main_lst = []
                if sudo[i][j] == 0:  # finding zeroes
                    net_lst = sq_list(sudo, [j, i]) + x_list(sudo, i) + y_list(sudo, j)
                    for num in range(0, 10):
                        if num not in net_lst:  # searching for number not contained in from 1 to 9
                            main_lst.append(num)
                    if len(main_lst) == 1:
                        sudo[i][j] = main_lst[0]
                    elif len(main_lst) == 0:
                        return 1
                    else:
                        continue
    if break_loop(sudo, ) == 0:  # break loop if no number remain zero
        return 0
    else:
        val = sudo_solver_2()  # recurrsion
        if val == 0:
            return 0
        if val == 1:
            return 1
# function 6


def sudo_solver_2():  # helper sudo solver, run when main_lst have more than one element left
    global sudo
    for i in range(0, 9):
        for j in range(0, 9):
            main_lst = []
            if sudo[i][j] == 0:  # finding zeroes
                net_lst = sq_list(sudo, [j, i]) + x_list(sudo, i) + y_list(sudo, j)
                for num in range(0, 10):
                    if num not in net_lst:  # searching for number not contained in from 1 to 9
                        main_lst.append(num)
                if len(main_lst) == 0:
                    return 1
                else:
                    for main_elem in main_lst:  # putting all possible value one by one and running sudo_solver again
                        sudo[i][j] = main_elem
                        deep_sudo = deepcopy(sudo)
                        val = sudo_solver()  # recurrsion
                        if val == 1:
                            sudo = deepcopy(deep_sudo)
                            continue
                        elif val == 0:
                            return 0
                    else:
                        return 1


if __name__ == "__main__":
    print('{:-^60}'.format('PROBLEM').center(150))
    print_board(sudo, offset=63)
    print("\n")
    sudo_solver()
    print('{:-^59}'.format('SOLUTION').center(150))
    print_board(sudo, offset=63)
