"""https://codility.com/media/train/10-Gcd.pdf"""
# notes
# a | b: a divides b. 2 | 6 = True; 6 | 2 = False
# ^mathematical notation, not python bitwise operator
# if greater int % smaller int == 0, gcd = smaller int
# otherwise gcd = gcd of larger *mod* smaller
# moddulo arithmetic: https://en.wikipedia.org/wiki/Modular_arithmetic
def gcd_sub(int_a, int_b):
    """Greatest common divisor by subtraction"""
    if int_a == int_b:
        return int_a
    if int_a > int_b:
        gcd_sub(int_a - int_b, int_b)
    else:
        gcd_sub(int_a, int_b - int_a)
def gcd_div(int_a, int_b):
    """Greatest common divisor by division"""
    if int_a % int_b == 0:
        result = int_b
    else:
        result = gcd_div(int_b, int_a % int_b)
    return result
def gcd_euc(int_a, int_b, res):
    """Greatest common divisor using binary Euclidean algorith"""
    if int_a == int_b:
        result = res * int_a
    elif (int_a % 2 == 0) and (int_b % 2 == 0):
        result = gcd_euc(int_a // 2, int_b // 2, 2 * res)
    elif int_a % 2 == 0:
        result = gcd_euc(int_a // 2, int_b, res)
    elif int_b % 2 == 0:
        result = gcd_euc(int_a, int_b // 2, res)
    elif int_a > int_b:
        result = gcd_euc(int_a - int_b, int_b, res)
    else:
        result = gcd_euc(int_a, int_b - int_a, res)
    return result
# debugging
# gcd_sub(15, 9)
# gcd_div(16, 10)
gcd_euc(17, 11, 1)
