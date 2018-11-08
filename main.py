'''
    Title: Precipitate Calculator
    Author: Long Tieu
    Date: 08-11-2018
'''

name = {
    "cl",
    "br",
    "i",
    "cu",
    "ag",
    "hg",
    "pb",
    "ti",
    "li",
    "mg",
    "ca",
    "sr",
    "ba",
    ""
}

def input_positive():
    name = input("Please enter the positive reacting ion. (no charges) ").lower()
    volume = float(input("What is the volume of the positive solution? (L) "))
    concentration = float("What is the concentration of the positive solution (mol/L) ")
    
    return name, volume, concentration

def input_negative():
    name = input("Please enter the negative reacting ion. (no charges) ").lower()
    volume = float(input("What is the volume of the negative solution? (L) "))
    concentration = float("What is the concentration of the negative solution (mol/L) ")
    
    return name, volume, concentration

def cal_mol(c, v):
    return c*v

def limiting_reagent(n1, co1, n2, co2, reactant1, reactant2):
    if (ratio1 >= ratio2):
        print("The limiting reagent is " + reactant2)
        return n2
    else:
        print("The limiting reagent is " + reactant1)
        return n1
    
def mass(n, M):
    return n*M

### --- CODE STARTS HERE --- ###
name1, v1, c1 = input_positive()
name2, v2, c2 = input_negative()
