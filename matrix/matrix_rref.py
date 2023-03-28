import cfg
import matrix_op


def RREF(matrix):

    row = 0
    for column in range(cfg.width): # we iterate the entire process by columns of matrix, but no definite row iteration
        #print("row: ", row)
        #print("col: ", column)
        if (matrix_op.close(matrix[row][column], 1)):#there is a pivot
            #print("pivot")
            row_subtractor(matrix, row, column)
            cfg.pivot_loc.append([row, column])
            row += 1 #move down

        elif (matrix_op.close(matrix[row][column], -1)):#there is almost  pivot loc = 1
            #print("-1 found")
            row_divider(matrix, row, column)
            row_subtractor(matrix, row, column)
            cfg.pivot_loc.append([row, column])
            row += 1 #move down

        elif (column == cfg.width - 1):# last row
            #print("last_row")
            #print(matrix[row][column])
            if(not matrix_op.close(matrix[row][column], 0)): #it could row divide by 0
                row_divider(matrix, row, column)
                row_subtractor(matrix, row, column)
                cfg.pivot_loc.append([row, column])
            else:
                cfg.free_var_loc.append(column) #make sure if a free var is in the last column it will be added

        elif (finder_bool(matrix, row, column) == True): # there is a 0 or a non 1 we should look for a better row but only from below our current row
            #print("moving column")
            finder_flipper(matrix, row, column)
            row_subtractor(matrix, row, column)
            cfg.pivot_loc.append([row, column])
            row += 1#move down
        else:
            #print("add free var")
            cfg.free_var_loc.append(column) #saving free var for nullspaces

        if (row == cfg.height): #the column was all 0 below we move to next column but don't change the row we are on
            break
        
    return None


def row_flipper(flipping_matrix, a, b):
    flipping_matrix[a], flipping_matrix[b] = flipping_matrix[b], flipping_matrix[a]
    cfg.determinant *= (-1)
    #print("flip: ", cfg.determinant)
    return None


def finder_flipper(working_matrix, start_row, problem_column):
    flag_flipped = False
    for y in range(start_row, cfg.height):
        if(matrix_op.close(working_matrix[y][problem_column], 1)): #we found a pivot candidate
            row_flipper(working_matrix, y, start_row)
            flag_flipped = True
            break #no point to keep looking

    for y in range(start_row, cfg.height): # we do the checking for 1 and -1 independently to prioritize 1 before -1 then random.
        if(matrix_op.close(working_matrix[y][problem_column], -1)): #special case for -1 to resolve the determinant correctly
            row_divider(working_matrix, start_row, problem_column) # in theory its not necessary
            flag_flipped = True
            break #no point to keep looking

    if (flag_flipped == False):#no good pivot candidate we need to just put a random one in and row divide
        for y in range(start_row, cfg.height):
            if(not matrix_op.close(working_matrix[y][problem_column], 0)):
                row_flipper(working_matrix, y, start_row)
                row_divider(working_matrix, start_row, problem_column)
                break #no point to keep looking
    return None


def finder_bool(working_matrix, start_row, problem_column):
    flag_non_zero = False
    for y in range(start_row, cfg.height):
        if(not matrix_op.close(working_matrix[y][problem_column], 0)):
            flag_non_zero = True
    return flag_non_zero


def row_divider(dividing_matrix, pivot_y, pivot_x):
    denominator = (dividing_matrix[pivot_y][pivot_x])
    for x in range(pivot_x, cfg.width_abs):
        dividing_matrix[pivot_y][x] = (dividing_matrix[pivot_y][x]) / denominator
    cfg.determinant *= denominator
    int_a_row(dividing_matrix, pivot_y)
    #print("div:", cfg.determinant)
    return None


def row_subtractor(subtracting_matrix, primary_row, pivot_col): #primary row and pivot col are just used to find the multiple, rows above and below pivot will be 0
    for y in range(0, cfg.height):
        if(y != primary_row): # rows
            multiple = subtracting_matrix[y][pivot_col]
            if(multiple != 0): # we don't want to multiple by 0
                #print("M = ", multiple) #testing line but helpful -----------
                for x in range(cfg.width_abs):#going across subtracting
                    subtracting_matrix[y][x] = (subtracting_matrix[y][x]) - multiple * (subtracting_matrix[primary_row][x])
                int_a_row(subtracting_matrix, y)
    return None


def int_a_row(matrix_int, row_num): #intigerizes a whole row of close numbers
    for x in range(cfg.width_abs):
        matrix_int[row_num][x] = matrix_op.int_a_num(matrix_int[row_num][x])
