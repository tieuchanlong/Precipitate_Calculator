'''
    Title: Precipitate Calculator
    Author: Long Tieu
    Date: 08-11-2018
'''

from math_library import *
from input_output import *

## Name of reactants in lower case
name = [
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
    "fe",
    "so4",
    "nh4",
    "no3",
    "clo3",
    "clo4",
    "ch3coo",
    "co3",
    "po4",
    "so3",
    "io3",
    "ooccoo",
    "oh"
]

## Name for output product
output_name = (
    "Cl",
    "Br",
    "I",
    "Cu",
    "Ag",
    "Hg",
    "Pb",
    "Ti",
    "Li",
    "Mg",
    "Ca",
    "Sr",
    "Ba",
    "Fe",
    "SO4",
    "NH4",
    "NO3",
    "ClO3",
    "ClO4",
    "CH3COO",
    "CO3",
    "PO4",
    "SO3",
    "IO3",
    "OOCCOO",
    "OH"
)

## Mass and charge of each reactants according to the "name" array
mass_charge = [
    [1, 35.45],
    [1, 79.9],
    [1, 126.9],
    [1, 63.546],
    [1, 107.87],
    [2, 200.59],
    [2, 207.2],
    [1, 204.3833],
    [1, 6.941],
    [2, 24.31],
    [2, 40.08],
    [2, 87.62],
    [2, 137.327],
    [2, 55.845],
    [2, 32.065],
    [1, 18.05],
    [1, 62.01],
    [1, 83.45],
    [1, 99.45],
    [1, 59.05],
    [2, 60.01],
    [3, 94.98],
    [2, 80.07],
    [1, 174.9],
    [2, 88.02],
    [1, 17.01]
]

# index list of each atom to access the precipitation and soluble list
index = [
    "nh4",
    "no3",
    "clo3",
    "clo4",
    "ch3coo",
    "f",
    "cl",
    "br",
    "i",
    "so4",
    "co3",
    "po4",
    "so3",
    "io3",
    "ooccoo",
    "oh"
]  

### --- Initiaste the precipitation and soluble arrays --- ###
precipitation = []
for i in range(10):
    precipitation.append([])
    if (i < 5):
        precipitation[i].append("rbclo4")
        precipitation[i].append("csclo4")
        precipitation[i].append("agch3coo")
        precipitation[i].append("hg2(ch3coo)2")
    elif (i == 5):
        precipitation[i].append("li")
        precipitation[i].append("mg")
        precipitation[i].append("ca")
        precipitation[i].append("sr")
        precipitation[i].append("ba")
        precipitation[i].append("fe")
        precipitation[i].append("hg")
        precipitation[i].append("pb")
    elif (i < 9):
        precipitation[i].append("cu")
        precipitation[i].append("ag")
        precipitation[i].append("hg")
        precipitation[i].append("pb")
        precipitation[i].append("ti")
    elif (i == 9):
        precipitation[i].append("ca")
        precipitation[i].append("sr")
        precipitation[i].append("ba")
        precipitation[i].append("ag")
        precipitation[i].append("hg")
        precipitation[i].append("pb")
        precipitation[i].append("ra")

soluble = []
for i in range(6):
    soluble.append([])
    if (i < 3):
        soluble[i].append("nh4")
    elif (i < 6):
        soluble[i].append("nh4")
        soluble[i].append("co(io3)2")
        soluble[i].append("fe2(ooccoo)3")
    elif (i == 6):
        precipitation[i].append("nh4")
        
        
## Search for the name of the reactants in the "name" array
def search_name(name1):
    for i in range(len(name)):
        if (name[i] == name1):
            break
        
    return i
        
def combine(name1, co1, name2, co2):  # This function combine two reactants together to make product to write in output
    if (search_name(name1.lower) <= 13 and co1 != 1):
        r = "(" + name1 + ")"
    else:
        r = name1
        
    if (co1 != 1):
        r += str(co1)
    
    
    if (search_name(name2.lower) <= 13 and co2 != 1):
        r += "(" + name2 + ")"
    else:
        r += name2
        
    if (co2 != 1):
        r += str(co2)
    
    return r

def check_solubility(a, b):
    for i in range(len(index)):
        if (b == index[i]):
            break
    
    if (i < 10):
        for j in range(len(precipitation[i])):
            if (precipitation[i][j] == a):
                return "slightly soluble"
        
        return "soluble"
    else:
        for j in range(len(soluble[i-10])):
            if (precipitation[i-10][j] == a):
                return "soluble"
        
        return "slightly soluble"


### --- CODE STARTS HERE --- ###
name1, v1, c1 = input_positive()
name2, v2, c2 = input_negative()

n1 = cal_mol(c1, v1)  # Mol of the first reactant
n2 = cal_mol(c2, v2)  # Mol of the second reactant  

coef1 = mass_charge[search_name(name2)][0]  # Coefficient of the first reactant
coef2 = mass_charge[search_name(name1)][0]  # Coefficient of the second reactant


u = gcd(max(coef1, coef2), min(coef1, coef2))  ## The greatest common divisor of two coefficients
coef1 = int(coef1/u)  # Simplify the reactants coefficients by dividing by their greatest common divisor in order to make the coefficient of the product 1
coef2 = int(coef2/u)


check, n = limiting_reagent(n1, coef1, n2, coef2, output_name[search_name(name1)], output_name[search_name(name2)])  ## Find the limiting reagent

if (check == 1):
    n = n / coef1  ## Find the mol of the product if the first reactant is the limiting reagent
else:
    n = n / coef2  ## Find the mol of the product if the second reactant is the limiting reagent
    
m = mass(n, (mass_charge[search_name(name1)][1] * coef1 + mass_charge[search_name(name2)][1] * coef2))  # Find the mass of the product
m = round(m, 2)

product_name = combine(output_name[search_name(name1)], coef1, output_name[search_name(name2)], coef2)

print_solubility(check_solubility(name1, name2))
print_mass(m, product_name)
