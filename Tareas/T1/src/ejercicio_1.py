'''
Created on 9 feb. 2020

@author: felipe, marco
'''
import os
from PIL import Image
from sympy.crypto.crypto import decipher_shift

def ejercicio_1_a_b(mensaje,inciso):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = open("resultados/Ejercicio_1_" + inciso + ".txt","w")
    for llave in range(len(alfabeto) + 1):
        resultado.write(decipher_shift(mensaje, llave, alfabeto) + " KEY: " + str(llave) + "\n")
        
def ejercicio_1_c(dir_imagen):
    image_bytes = bytearray(open(dir_imagen, "rb").read())
    for k in list(range(0,256)): 
        for i in range(len(image_bytes)):
            image_bytes[i] = (image_bytes[i] + k) % 256
        nombre = "resultados/Llave_" + str(k) + ".jpg"
        open(nombre, "wb").write(image_bytes)
        try:
            Image.open(nombre)
        except:
            os.remove(nombre)
        
if __name__ ==  "__main__":
    ejercicio_1_a_b("SLYDPYQCGLQNGPYBMPY","a")
    ejercicio_1_a_b("CVVCEMVJGKORNGOGPVCVKQP","b")
    ejercicio_1_c("recursos/imagen.enc")
    
    