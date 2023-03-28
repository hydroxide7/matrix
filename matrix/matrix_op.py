from math import floor
from math import ceil

import cfg

def close(a, b):
    return abs(a - b) < cfg.precision


def int_a_num(num):
    if (close(num, floor(num))):
        num = int(floor(num))
    elif (close(num, ceil(num))):
        num = int(ceil(num))
    return num


def frac(decimal): #tries to find a good fraction representation of numbers
    for denominator in range(2, cfg.max_denominator + 1):
        num = int_a_num(decimal * denominator)
        if (type(num) == int):
            output_text = str(num) + "/" + str(denominator)
            return output_text
    return decimal


def check_inconsistant(matrix):
    flag_zero = True
    for across in range(cfg.width):
        if (matrix[cfg.height-1][across] != 0):
            flag_zero = False
    if (flag_zero == True and matrix[len(matrix)-1][cfg.width_abs-1] != 0):
        return True
    
    return False
