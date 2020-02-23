'''
Created on 9 feb. 2020

@author: felipe, marco
'''
from sympy.core.numbers import igcdex

def ejercicio_7_a(a):
    return igcdex(a, 101)[0] % 101

def ejercicio_7_c(dir_archivo, key_a, key_b):
    imagen_bytes = bytearray(open(dir_archivo,"rb").read())
    for i in range(len(imagen_bytes)):
        imagen_bytes[i] = (key_a * (imagen_bytes[i] - key_b)) % 256
    open("resultados/Ejercicio_7.mp3","wb").write(imagen_bytes)


if __name__ == "__main__":
    ejercicio_7_c("recursos/audio.enc", 197, 255)
    print(ejercicio_7_a(99))