""" Name: Nia Bronson

Algorithm:
1. Set the speed of light equal to 300,000,000
2. Prompt the user for their mass number
3. Set the energy equal to (mass)(spped of light)^2
4. Display the entrensic energy
"""

## C means speed of light

c= int(299792458)

#M means mass

m= int(input("Please give me the mass of your object!"))

#E means intrensic energy of the object

E= ((m*c)**2)

print(E)
