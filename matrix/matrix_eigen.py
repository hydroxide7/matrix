from copy import deepcopy

import cfg

def char_poly_finder(matrix):
    add_depth(matrix)
    return cofactor_expansion (matrix)

def cofactor_expansion(matrix):
    line_row = 0
    partial_char_eqn = cfg.max_power * [0]
    
    if(len(matrix) == 2):
        return poly_sub (poly_multi(matrix[0][0],matrix [1][1]), poly_multi(matrix[0][1],matrix[1][0]))
    else:
        for line_col in range(len(matrix)): #go across that row it is crossed out
            cofa = poly_multi (matrix[line_row][line_col],cofactor_expansion(smaller_matrix (matrix,line_row,line_col)))
            
            if ((line_col+line_row)%2==0):
                partial_char_eqn = poly_add(partial_char_eqn, cofa)
            else:
                partial_char_eqn = poly_sub(partial_char_eqn,cofa)
            
    return partial_char_eqn

                      
def smaller_matrix(matrix, row_del, col_del):
    output_matrix = [[0 for x in range(len(matrix)-1)] for y in range(len(matrix)-1)]
    x = 0
    y = 0
    for down in range (len(matrix)):
        if(down != row_del):
            x = 0
            for across in range (len(matrix)):
                if(across != col_del):
                    output_matrix [y][x] = matrix [down][across]
                    x += 1
            y+=1
    return output_matrix

def poly_add(poly_a, poly_b):
    output_poly = cfg.max_power * [0]
    for power in range(cfg.max_power):
        output_poly[power] = poly_a[power] + poly_b[power]
    return output_poly

def poly_sub(poly_a,poly_b):
    output_poly = cfg.max_power * [0]
    for power in range(cfg.max_power):
        output_poly[power] = poly_a[power] - poly_b[power]
    return output_poly


def poly_multi(poly_a,poly_b): 
    output_poly = (len(poly_a)+len(poly_b)) * [0] #the len(output matrix) should be len(poly_a) + len(poly_b)
    for first in range(len(poly_a)): #each of poly_a needs to be multiplied by each of poly_b
        for second in range (len(poly_b)):
            output_poly [first+second] = output_poly [first+second] + poly_a[first] * poly_b[second]

    del output_poly [(cfg.max_power-len(output_poly)):] # removes unessessary powers. if copying code to somwere else remove this line it is specific to eigen
    return output_poly


def add_depth(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            constant = matrix[y][x]
            matrix[y][x] = cfg.max_power * [0] #x^n n can only be as big as width ***assumptption***
            matrix[y][x][0] = constant
            if(x == y):
                matrix[y][x][1] = -1


def eigen_vec (matrix,eigen_values):
    copy_matrix = deepcopy(matrix)
    for i in range(len(eigen_values)):
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                matrix [y][x]
