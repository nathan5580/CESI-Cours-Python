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

from math import *  # importation du module
print(cos(pi))
print(sqrt(25))