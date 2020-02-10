'''
Created on 9 feb. 2020

@author: felipe, marco
'''
import os
import threading

from sympy.crypto.crypto import decipher_shift
from PIL import Image

def a(mensaje):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for llave in range(len(alfabeto) + 1):
        print(decipher_shift(mensaje, llave, alfabeto) + " KEY: " + str(llave))
    print("===========================================================================")
    
    for llave in range(len(alfabeto) + 1):
        print(decipher_shift(mensaje, -llave, alfabeto) + " KEY: " + str(-llave))
        
def a_c_aux(lista_llaves, imagen_bits):
    for k in lista_llaves:
        for indice,valor in enumerate(imagen_bits):
            imagen_bits[indice]=(imagen_bits[indice] + k) % 256
        nombre = "resultados/Llave_" + str(k) + ".jpg"
        resultado = open(nombre, "wb")
        resultado.write(imagen_bits)
        try:
            Image.open(nombre)
            print("OK")
            return
        except:
            print("Except")
            os.remove(nombre)
            
def a_c(nombre_imagen):
    lista_aux = []
    aux = 0
    for i in range(7):
        lista_aux.append(list(range(aux,aux + 32)))
        aux += 32
    print(lista_aux)
    file = open(nombre_imagen, "rb")
    imagen_leida = file.read()
    imagen_bits = bytearray(imagen_leida)
    for l in lista_aux:
        hilo = threading.Thread(target=a_c_aux,args=(l,imagen_bits))
        hilo.start()
        
        
if __name__ ==  "__main__":
    #a("SLYDPYQCGLQNGPYBMPY")
    #a("CVVCEMVJGKORNGOGPVCVKQP")
    a_c("recursos/imagen.enc")
    
    