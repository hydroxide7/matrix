import cfg


def printer(printing_matrix): # not boroko lol
    for y in range(cfg.height):
        print("[", end="")
        for x in range(cfg.width_abs):
            if (printing_matrix[y][x] == None): #checking to print "x"s
                print("x", end="")
            else:
                print(printing_matrix[y][x], end="")

            if(x == cfg.width - 1 and cfg.width != cfg.width_abs):
                print("|\t", end="")
            elif (x != cfg.width_abs - 1): #check for comma placment
                print(",\t", end="")
        print("]")
    return None


def inputer(inputing_matrix):
    for y in range(cfg.height):
        for x in range(cfg.width_abs):

            inputing_matrix[y][x] = None
            printer(inputing_matrix)

            print(x, y, end="")
            inputing_matrix[y][x] = int(input(": "))
        printer(inputing_matrix)
    return None

#--- basis problem printer functions! ---


def rowspace_printer(matrix_data, pivots):
    if(len(cfg.pivot_loc) != 0):
        for count in range(len(pivots)): #this is going down
            print("(", end="")
            for x in range(cfg.width): # across
                print(matrix_data[pivots[count][0]][x], end="")
                if (x != cfg.width_abs - 1): #check for comma placment
                    print(",", end="")
            if (count != len(cfg.pivot_loc) - 1):
                print(")", end=",")
            else:
                print(")", end="")
        print("")
    else:
        print("n/a")
    return None


def columnspace_printer(matrix_data, pivots):
    if(len(cfg.pivot_loc) != 0):
        for y in range(cfg.height): #going down

            for across in range(len(pivots)):#across
                if (y == 0):
                    print("/", end="")
                    if (matrix_data[y][pivots[across][1]] >= 0):
                        print(" ", end="")
                    print(matrix_data[y][pivots[across][1]], end=" ")
                    print("\\", end="")

                elif (y == cfg.height - 1):
                    print("\\", end="")
                    if (matrix_data[y][pivots[across][1]] >= 0):
                        print(" ", end="")
                    print(matrix_data[y][pivots[across][1]], end=" ")
                    print("/", end="")
                else:
                    print("|", end="")
                    if (matrix_data[y][pivots[across][1]] >= 0):
                        print(" ", end="")
                    print(matrix_data[y][pivots[across][1]], end=" ")
                    print("|", end="")
            print("")
    else:
        print("n/a")
    return None


def nullspace_printer(matrix_data, pivots):
    if(len(cfg.pivot_loc) != cfg.width):
        for y in range(cfg.height): #going down
            for across in range(cfg.width):#across
                flag_column_pivot = False
                for check in range(len(pivots)): #check if the "across" we are on is one with a pivot, we only want non pivots
                    if(across == pivots[check][1]):
                        flag_column_pivot = True

                if (flag_column_pivot == False):
                    if (y == 0):
                        print("/", end="")
                        if (matrix_data[y][across] >= 0):
                            print(" ", end="")
                        print(matrix_data[y][across], end=" ")
                        print("\\", end="")

                    elif (y == cfg.height - 1):
                        print("\\", end="")
                        if (matrix_data[y][across] >= 0):
                            print(" ", end="")
                        print(matrix_data[y][across], end=" ")
                        print("/", end="")
                    else:
                        print("|", end="")
                        if (matrix_data[y][across] >= 0):
                            print(" ", end="")
                        print(matrix_data[y][across], end=" ")
                        print("|", end="")

            print("")
    else:
        print("n/a")
    return None


def determinant_printer(matrix_data):
    if (cfg.height == cfg.width):
        print(cfg.determinant)
    else:
        print("must be a square matrix!")
