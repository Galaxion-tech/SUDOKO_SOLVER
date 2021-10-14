from copy import deepcopy
# j= 0,1,2,3,4,5,6,7,8
sudo = [[0, 0, 0, 0, 6, 0, 0, 0, 0],  # i=0
        [0, 5, 0, 0, 0, 0, 2, 0, 0],  # i=1
        [0, 0, 0, 5, 3, 8, 0, 0, 0],  # i=2
        [8, 0, 5, 0, 0, 0, 0, 4, 0],  # i=3
        [9, 0, 0, 0, 4, 5, 0, 0, 8],  # i=4
        [4, 0, 0, 8, 0, 1, 6, 0, 2],  # i=5
        [5, 0, 0, 0, 0, 0, 7, 2, 4],  # i=6
        [0, 0, 0, 0, 0, 4, 0, 8, 0],  # i=7
        [0, 2, 0, 6, 0, 0, 5, 0, 9]]  # i=8
# function 1


def sq_list(inp):  # inp is list of coordinates (x,y) or (j,i)
    x = int(inp[0]/3)
    y = int(inp[1]/3)
    sq_lst = []
    for i in range(3*y, 3*(y+1)):
        for j in range(3*x, 3*(x+1)):
            sq_lst.append(sudo[i][j])
    return sq_lst
# function 2


def x_list(y):  # here y is an integer which collect horizontal row
    return sudo[y]
# function 3


def y_list(x):  # here x is an integer which collect vertical row
    y_lst = []
    for row in sudo:
        y_lst.append(row[x])
    return y_lst
# function 4


def break_loop():  # help in breaking sudo-solver function
    for i in range(0, 9):
        if 0 in sudo[i]:
            return 1
    else:
        return 0
# function 5


def sudo_solver():  # main function
    global sudo
    for repetition in range(0, 10):  # repeating for 10 times
        for i in range(0, 9):
            for j in range(0, 9):
                main_lst = []
                if sudo[i][j] == 0:  # finding zeroes
                    net_lst = sq_list([j, i]) + x_list(i) + y_list(j)
                    for num in range(0, 10):
                        if num not in net_lst:  # searching for number not contained in from 1 to 9
                            main_lst.append(num)
                    if len(main_lst) == 1:
                        sudo[i][j] = main_lst[0]
                    elif len(main_lst) == 0:
                        return 1
                    else:
                        continue
    if break_loop() == 0:  # break loop if no number remain zero
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
                net_lst = sq_list([j, i]) + x_list(i) + y_list(j)
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


# _main_
print("-------------------------PROBLEM---------------------------".center(150))
print("\n")
for i in sudo:
    print(" "*60, i)
print("\n")
sudo_solver()
print("-------------------------SOLUTION---------------------------".center(150))
print("\n")
for i in sudo:
    print(" "*60, i)
