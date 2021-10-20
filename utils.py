# function 1
def sq_list(sudo, inp):  # inp is list of coordinates (x,y) or (j,i)
    x = int(inp[0]/3)
    y = int(inp[1]/3)
    sq_lst = []
    for i in range(3*y, 3*(y+1)):
        for j in range(3*x, 3*(x+1)):
            sq_lst.append(sudo[i][j])
    return sq_lst
# function 2


def x_list(sudo, y):  # here y is an integer which collect horizontal row
    return sudo[y]
# function 3


def y_list(sudo, x):  # here x is an integer which collect vertical row
    y_lst = []
    for row in sudo:
        y_lst.append(row[x])
    return y_lst
# function 4


def break_loop(sudo, ):  # help in breaking sudo-solver function
    for i in range(0, 9):
        if 0 in sudo[i]:
            return 1
    else:
        return 0
# function 5
