# -*- coding: utf-8 -*-
from sympy import mod_inverse
from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'



def xx_reverse(x,k):
 """
 Hace un XOR entre cada uno de los bytes de el archivo
 x pasado como parametro y el arreglo aleatorio de bytes k
 """

 with open(x.replace('.enc','') ,'wb') as z:
  z.write((lambda x:bytes([x[i] ^ k[i % 16] for i in range(len(x))]))(open(x,'rb').read()))
 os.remove(x)
 

if __name__ == "__main__":
    print("Ejecutando vacuna ███▒▒▒▒▒▒▒")
    _,_,x = next(os.walk('./'))
    #x.remove(argv[0])
    x.remove("juego.py")
    x.remove("vacuna.py")
    
    
    with open('.xyz','rb') as reverse:
        data = reverse.read()
        c = data[0:1]
        d = data[1:33]
        k = data[33:]

        
    c_int = int.from_bytes(c, 'big')
    d_int = int.from_bytes(d, 'big')
    k_int = int.from_bytes(k, 'big')
    
    inverso = mod_inverse(d_int,(1 << c_int))
    key = (inverso * k_int) % (1 << c_int)
    key_b = key.to_bytes(32,'big')
    c = 0
    for i in key_b:
        if i == 0:
            c += 1
    key_final = key_b[c:]
    
    for file in x:
        xx_reverse(file,key_final)
    
    print("Efectos revertidos, NO depositar nada (⌐■_■)")
    
    