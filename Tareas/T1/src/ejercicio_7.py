'''
Created on 9 feb. 2020

@author: felipe, marco
'''

from sympy.crypto.crypto import decipher_affine,encipher_affine

alfabeto = ""
for i in range(101):
    alfabeto += str(i) 
print(alfabeto)


print (encipher_affine("100", (99,20), alfabeto))
