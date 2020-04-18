#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 9 feb. 2020

@author: felipe, marco
'''
from random import randint
from os import urandom

def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a

def n(n):
    for i in range(n):
        print(n = n*10)
        
        
def rc4_encrypt(key):
    # Inicialización
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256
        box[i], box[x] = box[x], box[i]

    # Generación de bytes pseudoaleatorios y cifrado
    x = 0
    y = 0
    out = []
    for byte in range(256):
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(box[(box[x] + box[y]) % 256])
    return bytes(out)

def randint_algorithm(n):
    count = 0
    for x in range(n):
        a = randint(0, 2**(8*7)-1)
        b = randint(0, 2**(8*7)-1)
        if(mcd(a,b) == 1):
            count += 1
    print("El número de primos relativos que se contaron con n = ",n,"fueron",count)
    
def urandom_algorithm(n):
    count = 0
    for x in range(n):
        a = urandom(7)
        b = urandom(7)
        c = int.from_bytes(a, byteorder='big')
        d = int.from_bytes(b, byteorder='big')
        if(mcd(c,d) == 1):
            count += 1
    print("El número de primos relativos que se contaron con n = ",n,"fueron",count)
    
    
def rc4_algorithm(n):
    count = 0
    for x in range(n):
        a = rc4_encrypt(urandom(4))
        b = rc4_encrypt(urandom(4))
        c = int.from_bytes(a, byteorder='big')
        d = int.from_bytes(b, byteorder='big')
        if(mcd(c,d) == 1):
            count += 1
    print("El número de primos relativos que se contaron con n = ",n,"fueron",count)



if __name__ == "__main__":
    
    # RADINT
    print("RADINT")
    randint_algorithm(100)
    randint_algorithm(1000)
    randint_algorithm(10000)
    
    # URANDOM
    print("URANDOM")
    urandom_algorithm(100)
    urandom_algorithm(1000)
    urandom_algorithm(10000)
    
    # RC4
    print("RC4")
    rc4_algorithm(100)
    rc4_algorithm(1000)
    rc4_algorithm(10000)
    
    
    