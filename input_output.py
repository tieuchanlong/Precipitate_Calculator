'''
    This is input and output functions file.
'''

### --- Inputs --- ###
def input_positive():
    name = input("Please enter the positive reacting ion. (no charges) ").lower()
    volume = float(input("What is the volume of the positive solution? (L) "))
    concentration = float(input("What is the concentration of the positive solution (mol/L) "))
    
    return name, volume, concentration

def input_negative():
    name = input("Please enter the negative reacting ion. (no charges) ").lower()
    volume = float(input("What is the volume of the negative solution? (L) "))
    concentration = float(input("What is the concentration of the negative solution (mol/L) "))
    
    return name, volume, concentration



### --- Outputs --- ###
def print_mass(mass, product_name):
    print("The mass of " + product_name + " is " + str(mass) + " grams.")
    
def print_solubility(status):
    print("The product is " + status + ".")