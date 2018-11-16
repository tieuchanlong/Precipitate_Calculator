'''
    This is a math library.
'''


### --- Normal math section --- ###
def max(a, b):
    if (a >= b):
        return a
    else:
        return b
    
def min(a, b):
    if (a <= b):
        return a
    else:
        return b
    
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
    
    
### --- Chemistry math section --- ###
def cal_mol(c, v):
    return c*v

def limiting_reagent(n1, co1, n2, co2, reactant1, reactant2):
    if (n1/ co1 >= n2/ co2):
        print("The limiting reagent is " + reactant2 + ".")
        return 2, n2
    else:
        print("The limiting reagent is " + reactant1 + ".")
        return 1, n1
    
def mass(n, M):
    return n*M