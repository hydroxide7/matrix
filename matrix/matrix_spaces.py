import cfg

def determinant_check(matrix):
    flag_number = False
    for i in range(cfg.width):
        if (matrix[-1][i] != 0): #last row will be the ones with 0s row if there is one
            flag_number = True
            break
    if (flag_number == False):
        cfg.determinant = 0
    return None
          
def nullspace_finder(input_matrix):
    #print ("start finder ===========")
    #print (cfg.pivot_loc)
    #print (cfg.free_var_loc)
    nullspace_matrix = [[0 for x in range(len(cfg.free_var_loc)+1)] for y in range(cfg.width)] #len(cfg.free_var_loc) + 1 is the num of free vars + a constant
    
    pivot_check = 0
    next_free_var = 1
    for variable_num in range(cfg.width): #going across x1 x2 x3....
        if (variable_num == cfg.pivot_loc[pivot_check][1]): # is pivot
            #print ("pivot")
            
            if(cfg.width_abs != cfg.width):
                nullspace_matrix[variable_num][0] = (-1) * input_matrix[variable_num][cfg.width_abs-1]
                
            counter_fv_loc = 1
            #print ("var_num : ", variable_num )
            #print ("couunter_fv: ", counter_fv_loc )
            #print ("pivot_check: ", pivot_check)
            for across in cfg.free_var_loc:
                #print ("across: ", across) #the nth x, going across each free var = the y height of the found piot, going across to print each line.
                nullspace_matrix[variable_num][counter_fv_loc] = (-1) * input_matrix[cfg.pivot_loc[pivot_check][0]][across] #i hate this line of code
                #print(nullspace_matrix) 
                counter_fv_loc += 1
            if(pivot_check < len(cfg.pivot_loc)-1): #overflow protection
                pivot_check += 1
                
        else: #is a free var
            #print("free")
            nullspace_matrix [variable_num][next_free_var] = 1 #his x column was a free variable_num
            #print(nullspace_matrix)
            if(next_free_var < len(cfg.free_var_loc)): #overflow protection
                next_free_var += 1    
    #print(nullspace_matrix)            
    return nullspace_matrix
