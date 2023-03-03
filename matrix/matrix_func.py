from math import floor
from math import ceil

import cfg
import matrix_io


def RREF(matrix):

    row = 0
    for column in range(cfg.width): # we iterate the entire process by columns of matrix, but no definite row iteration

        if (close(matrix[row][column], 1)):#there is a pivot loc = 1
            print ("pivot")
            row_subtractor(matrix, row, column)
            cfg.pivot_loc.append([row, column])
            row += 1 #move down

        elif (finder_bool(matrix, row, column) == True): # there is a 0 or a non 1 we should look for a better row but only from below our current row
            finder_flipper(matrix, row, column)
            row_subtractor(matrix, row, column)
            cfg.pivot_loc.append([row, column])
            row += 1#move down
        if (row == cfg.height):
            break
        matrix_io.printer(matrix)
        determinant_check(matrix_data) # checking for a 0 row to make the determinat 0
    #the column was all 0 below we move to next column but don't change the row we are on
    return None


def close(a, b):
    return abs(a - b) < cfg.precision


def row_flipper(flipping_matrix, a, b):
    flipping_matrix[a], flipping_matrix[b] = flipping_matrix[b], flipping_matrix[a]
    cfg.determinant *= (-1)
    print ("flip: ",cfg.determinant)
    return None


def finder_flipper(working_matrix, start_row, problem_column):
    flag_flipped = False
    for y in range(start_row, cfg.height):
        if(close(working_matrix[y][problem_column], 1)): #we found a pivot candidate
            row_flipper(working_matrix, y, start_row)
            flag_flipped = True
            break #no point to keep looking
        
    for y in range(start_row, cfg.height): # we do the checking for 1 and -1 independantly to prioritize 1 before -1 then random.
        if(close(working_matrix[y][problem_column], -1)): #special case for -1 to resolve the determinant corectly
            row_divider(working_matrix,start_row,problem_column) # in theory its not nessesary
            flag_flipped=True
            break #no point to keep looking

    if (flag_flipped == False):#no good pivot candidate we need to just put a random one in and row divide
        for y in range(start_row, cfg.height):
            if(not close(working_matrix[y][problem_column], 0)):
                row_flipper(working_matrix, y, start_row)
                row_divider(working_matrix, start_row, problem_column)
                break #no point to keep looking
    return None


def finder_bool(working_matrix, start_row, problem_column):
    flag_number = False
    for y in range(start_row, cfg.height):
        if(not close(working_matrix[y][problem_column], 0)):
            flag_number = True
    return flag_number


def row_divider(dividing_matrix, pivot_y, pivot_x):
    denominator = (dividing_matrix[pivot_y][pivot_x])
    for x in range(pivot_x, cfg.width_abs):
        dividing_matrix[pivot_y][x] = (dividing_matrix[pivot_y][x]) / denominator
    cfg.determinant *= denominator
    int_a_row(dividing_matrix, pivot_y)
    print ("div:", cfg.determinant)
    return None


def row_subtractor(subtracting_matrix, primary_row, pivot_col): #primary row and piviot col are just used to find the multiple, rows above and below pivot will be 0
    for y in range(0, cfg.height):
        if(y != primary_row):
            multiple = subtracting_matrix[y][pivot_col]
            if(multiple != 0): # we don't want to multiple by 0
                print("M = ", multiple) #testing line but helpful -----------
                for x in range(cfg.width_abs):
                    subtracting_matrix[y][x] = (subtracting_matrix[y][x]) - multiple * (subtracting_matrix[primary_row][x])
    return None


def int_a_row(matrix_int, row_num): #intigerizes a whole row of close numbers
    for x in range(0, cfg.width_abs):
        if (close(matrix_int[row_num][x], floor(matrix_int[row_num][x]))):
            matrix_int[row_num][x] = int(floor(matrix_int[row_num][x]))
        elif (close(matrix_int[row_num][x], ceil(matrix_int[row_num][x]))):
            matrix_int[row_num][x] = int(ceil(matrix_int[row_num][x]))
    return None

def determinant_check (matrix):
    flag_number = False
    for i in range (cfg.width):
        if (matrix[-1][i] !=0): #last row will be the ones with 0s row if ther is one
            flag_number = True
    if (flag_number == False):
        cfg.determinant = 0
    