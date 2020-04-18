#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 9 feb. 2020

@author: felipe, marco
'''

from os import urandom
from random import randint
from RC4 import rc4_encrypt


def n(n):
    for i in range(n):
        print(n=n * 10)


def randint_algorithm(n):
    count = 0
    for x in range(n):
        a = randint(0, 2 ** (8 * 7) - 1)
        b = randint(0, 2 ** (8 * 7) - 1)
        if(mcd(a, b) == 1):
            count += 1
    print("El número de primos relativos que se contaron con n = ", n, "fueron", count)


def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a


if __name__ == "__main__":
    randint_algorithm(100)
    randint_algorithm(1000)
    randint_algorithm(10000)
