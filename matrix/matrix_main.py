from copy import deepcopy

import cfg
import matrix_rref
import matrix_io
import matrix_op
import matrix_spaces
import matrix_eigen
import poly_solve #spcial thanks xav

class MatrixSizeError(LookupError):
    '''for error handling'''    

#======== math puts the fun in function!=======

#=================== main =================
print("Welcome to the linear algebra help calculator!")
while (1 == 1):
    cfg.reset()
    print("What can I help you with?")
    print("(1): RREF")
    print("(2): RREF with columnspace, rowspace, and nullspace for determinant")
    print("(3): Eigin values and vectors")
    print("(a): Change calculation precision")
    print("(b): Change output precision")
    print("(c): Change max denominator check")
    print("(q): Quit")
    print("Enter the number or letter corresponding to what function you would like to use:")
    input_value = input()
    
    #-----------------
    if(input_value == '1'):#RREF
        cfg.width_abs = int(input("enter width of the entire matrix: "))
        cfg.width = int(input("enter width of the coefficient matrix: ")) #cfg.width_abs needs to be bigger then cfg.width

        if (cfg.width_abs < cfg.width):
            raise MatrixSizeError("the entire matrix must be bigger or equal to coefficient matrix!")

        
        cfg.height = int(input("enter height: "))
        matrix = [[0 for x in range(cfg.width_abs)] for y in range(cfg.height)]

        matrix_io.inputer(matrix)
        matrix_rref.RREF(matrix)
        print ("final: ")       
        matrix_io.printer(matrix)
    #-----------------
    if(input_value == '2'): #rowspace, columnspace, nullspace
        cfg.width_abs = int(input("enter width of the entire matrix: "))
        cfg.width = int(input("enter width of the coefficient matrix: ")) #cfg.width_abs needs to be bigger then cfg.width
        
        if (cfg.width_abs < cfg.width):
            raise MatrixSizeError("the entire matrix must be bigger or equal to coefficient matrix!")
        if (cfg.width_abs  > 1 + cfg.width):
            raise MatrixSizeError("the augmented matrix can only have a 1 wide right hand side!")        

        cfg.height = int(input("enter height: "))
        
        cfg.width_abs = 6
        cfg.width = 6
        cfg.height = 5
        
        matrix = [[0 for x in range(cfg.width_abs)] for y in range(cfg.height)]
        cfg.pivot_loc = []
        
        """
        matrix = [
        [1,-2,1,1,1],
        [-2,4,-1,0,1],
        [-1,2,0,1,0],
        [2,-4,0,-2,-2]
        ]
        
        matrix = [
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        ]
        """
        matrix_io.inputer(matrix)
        saver = deepcopy(matrix)
        matrix_rref.RREF(matrix)
        print ("final: ")
        matrix_io.printer(matrix)
        
        if(cfg.width_abs > cfg.width and matrix_op.check_inconsistant(matrix)): #it is inconsistant:
            print ("inconsistant")
        else:
            
            print("free var loc", cfg.free_var_loc)
            #this must be after rref because the size of free_var_loc is 0 before the rref builts that list
    
            print("the pivot location is: ")
            print(cfg.pivot_loc)
    
            print("columnspace: ")
            matrix_io.columnspace_printer(saver)
            
            nullspace_matrix = matrix_spaces.nullspace_finder(matrix)
            print("parametric form")
            matrix_io.parametric_printer(nullspace_matrix)
            print("nullspace: ")
            matrix_io.nullspace_printer(nullspace_matrix)
    
            print("Rowspace:")
            print("RREF: ", end="")
            matrix_io.rowspace_printer(matrix)
            print("or")
            print("original: ", end="")
            matrix_io.rowspace_printer(saver)
    #---------------
    if(input_value == '3'):
        cfg.width_abs = int(input("enter one side length of the matrix: ")) #cfg.width_abs needs to be bigger then cfg.width
        cfg.height = cfg.width_abs
        cfg.width = cfg.width_abs #width should not be used, but here to protect io libary functions
        cfg.max_power = cfg.width_abs + 1
        
        matrix = [[0 for x in range(cfg.width)] for y in range(cfg.height)]
        """
        cfg.height = 5
        cfg.width = 5
        cfg.width_abs = 5
        cfg.max_power = 6 
        
        matrix = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25],
        ]        
        """
        matrix_io.inputer(matrix)
        
        saver = deepcopy(matrix)
        print(saver)
        char_poly = matrix_eigen.char_poly_finder(matrix) # after this line matrix is completely f-ed, don't use it
        print ("characteristic polynomial:",char_poly)
        
        eigen_values = poly_solve.poly_roots(char_poly)
        print ("eigen values:",eigen_values)
        
        #[-3.642080737002, 0, 68.642080737002]
        print ("eigen vectors:")
        for counter in range(len(eigen_values)):
            cfg.pivot_loc = [] #reset these list to work correctly
            cfg.free_var_loc = []              
            working_matrix = deepcopy(saver)
            for y in range(cfg.height):
                for x in range(cfg.width):
                    if (y == x):
                        working_matrix[y][x] = working_matrix[y][x] - eigen_values[counter]
            matrix_rref.RREF(working_matrix) 
            nullspace_vectors= matrix_spaces.nullspace_finder(working_matrix)
            matrix_io.nullspace_printer(nullspace_vectors)      
         
    #=======options menu===========
    if(input_value == 'a'):
        print("Enter the calculation precision you would like to use: ")
        cfg.precision = float(input())
    if(input_value == 'b'):
        print("Enter the output precision you would like to use: ")
        cfg.output_precision = float(input())
    if(input_value == 'c'):
        print("Enter the max denominator you would like to check too")
        cfg.max_denominator = float(input())            
        
    if(input_value == 'q'):
        print("Goodbye, have a nice day!")
        break
