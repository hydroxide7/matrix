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
            elif (x != cfg.width_abs - 1): #check for comma placement
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
                if (x != cfg.width_abs - 1): #check for comma placement
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

def parametric_printer(null_matrix_data):
    free_var_names = ["s","t","r"]
    half_down = cfg.width//2
    for y in range(cfg.width): #going down, width for nullspace matrix 
        for across in range(len(cfg.free_var_loc)):#across
            if (y == 0):
                print("/", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("\\", end="")

            elif (y == cfg.width - 1):
                print("\\", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("/", end="")
            else:
                print("|", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("|", end="")
            
            if(across != len(cfg.free_var_loc)):
                if(y != half_down):
                    print (" ", end = " ")
                else:
                    if(across != 0):
                        if(across > 3):
                            print("x"+ str (across),end="")
                        else:
                            print (free_var_names[across -1], end = " ")
                    else:
                        print("c", end=" ")
                
        print("")#new line for next across         
            
                

    """
    for x in range(len(cfg.free_var_loc) + 1): # go across print down
        for y in range(cfg.width):
            if (y == 0)
            
            
            if (y == 0): #first
                print ("/", null_matrix_data[y][x],"\\", end = "")
            elif (y == len(cfg.free_var_loc)-1): #last
                print ("\\", null_matrix_data[y][x],"/", end = "")
            else: #middle
                print ("|", null_matrix_data[y][x],"||", end = "")
            if (y == half_down and x != 0):
                if (x > 4):
                    print ("x",x-1)
                else:
                    print (free_var_name[x-1])
    """
                
def nullspace_printer(null_matrix_data):
    #go across then down
    half_down = cfg.width//2
    
    for y in range(cfg.width): #going down, width for nullspace matrix 
        for across in range(1,len(cfg.free_var_loc)):#across
            if (y == 0):
                print("/", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("\\", end="")

            elif (y == cfg.width - 1):
                print("\\", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("/", end="")
            else:
                print("|", end="")
                if (null_matrix_data[y][across] >= 0):
                    print(" ", end="")
                print(null_matrix_data[y][across], end=" ")
                print("|", end="")
        print("")#new line for next across         

    return None


def determinant_printer(matrix_data):
    if (cfg.height == cfg.width):
        print(cfg.determinant)
    else:
        print("must be a square matrix!")
