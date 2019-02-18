"""voici ma belle documentation sur plusieurs lignes
ligne 1
ligne 2
ligne 3"""

#simples print

a = b = c = 1
print(a)
print(b)
print(c)

counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string print counter

print(miles)
print(counter)
print(name)

# Listes

list = [ 'abcd', 123 , 1.23, 'efgh', 45.6 ]
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element

#conversion de variables
"""
int() , long(),float(),complex()
str(), chr()
Eval() --> to object
tuple(), list(), set()
dict()
Unichr(),ord(),hex(),oct()
+,-,*,/
%,**,// (mod / puissance et division)
"""
#import ect

#import sys; x = 'foo' : importations
#input("attendre input")

#dictionry
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

import math # importation du module
print(math.cos(math.pi))
print(math.sqrt(25))

#lire un fichier
contenu = open("demofile.txt")
for line in contenu:
    print(line)
    if line.startswith('error'):
        print("j'ai trouvé l'erreur !")
print("End of file")

# condition façon ternaire
maVar = 100
if(maVar == 100): print ("test variable")

#Iteration sur des lettres
for letter in 'Python':
    print(letter)

# Definition d'une fonction
def PrintTest(strToPrint):
   print(strToPrint)

PrintTest("je suis un texte")

#module
import moduleCesi
moduleCesi.PrintFromModule("je suis dans le module")

# yakoi dans mon module
for mod in dir(math):
    print(mod)

# yakoi
#globals()
#locals()

# tous les modules existants
#help('modules') # trop lonnnnng

# import de modules
import Armors
Armors.mark_I()