from copy import deepcopy

import cfg
import matrix_func
import matrix_io


class MatrixSizeError(LookupError):
    '''for error handling'''

#======== math puts the fun in function!=======


#=================== main =================
flag_continue = True

print("Welcome to the linear algebrea help calulator!")
while (flag_continue == True):
    print("What can I help you with?")
    print("(1): RREF")
    print("(2): RREF with columnspace, rowspace, and nullspace + determinant")
    print("(a): Change Precision")
    print("(q): Quit")
    print("Enter the number or letter corresponding to what function you would like to use:")
    cfg.input_value = input()

    if(cfg.input_value == '1'):#RREF
        cfg.width_abs = int(input("enter width of the entire matrix: "))
        cfg.width = int(input("enter width of the coeffcient matrix: ")) #cfg.width_abs needs to be bigger then cfg.width

        if (cfg.width_abs < cfg.width):
            raise MatrixSizeError("the entire matrix must be bigger or equal to coefficient matrix!")

        cfg.height = int(input("enter height: "))
        matrix = [[0 for x in range(cfg.width_abs)] for y in range(cfg.height)]

        matrix_io.inputer(matrix)
        matrix_func.RREF(matrix)
        matrix_io.printer(matrix)
#-----------------
    if(cfg.input_value == '2'): #rowspace, columnspace, nullspace
        cfg.width_abs = int(input("enter width of matrix: "))
        cfg.height = int(input("enter height of matrix: "))

        cfg.width = cfg.width_abs
        matrix = [[0 for x in range(cfg.width_abs)] for y in range(cfg.height)]
        cfg.pivot_loc = []
        
        matrix_io.inputer(matrix)
        saver = deepcopy(matrix)
        matrix_func.RREF(matrix)
        matrix_io.printer(matrix)

        print("the pivot location is: ")
        print(cfg.pivot_loc)

        print("columnspace: ")
        matrix_io.columnspace_printer(saver, cfg.pivot_loc)

        print("nullspace: ")
        matrix_io.nullspace_printer(saver, cfg.pivot_loc)

        print("Rowspace:")
        print("RREF: ", end="")
        matrix_io.rowspace_printer(matrix, cfg.pivot_loc)
        print("or")
        print("original: ", end="")
        matrix_io.rowspace_printer(saver, cfg.pivot_loc)

        print("determinant:")
        matrix_io.determinant_printer(matrix)

#=======options menu===========
    if(cfg.input_value == 'a'):
        print("Enter the precistion you would like to use: ")
        cfg.precision = float(input())
    if(cfg.input_value == 'q'):
        print("Goodbye, have a nice day!")
        flag_continue = False
