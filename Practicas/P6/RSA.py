#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prime_generator import generate_prime
from random import randint
from utils import elige_e
from sympy import mod_inverse

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        self.p = generate_prime(randint(100,256))
        self.q = generate_prime(randint(100,256))
        self.n = self.p * self.q
        self.pub_key = elige_e(self.__phi__())
        self.priv_key = mod_inverse(self.pub_key,self.__phi__())
        self.padding_scheme = False
        
        pub = open('pub_key.pem','w')
        pub.write(str(self.n) + '/n')
        pub.write(str(self.pub_key) + '/n')
        pub.close()
        
        priv = open('priv_key.pem','w')
        priv.write(str(self.n) + '\n')
        priv.write(str(self.priv_key) + '\n')
        priv.close()

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        return (self.p - 1) * (self.q - 1)
 
    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        criptotext = [] 
        for letter in message:
            criptotext.append(pow(ord(letter),self.pub_key,self.n))
        return criptotext
        

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        message = ''
        for num in criptotext:
            message += chr(pow(num, self.priv_key,self.n))
        return message
    
    
if __name__ == "__main__":
    rsa = RSA()
    print(rsa)
    
    
    
