# -*- coding: utf-8 -*-
from sympy import mod_inverse
from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'



def xx(x,k):
 """
 Hace un XOR entre cada uno de los bytes de el archivo
 x pasado como parametro y el arreglo aleatorio de bytes k
 """

 with open(x.replace('.enc','') ,'wb') as z:
  z.write((lambda x:bytes([x[i] ^ k[i % 16] for i in range(len(x))]))(open(x,'rb').read()))
 #os.remove(x + '.enc')
 

if __name__ == "__main__":
    _,_,x = next(os.walk('./'))
    #x.remove(argv[0])
    x.remove("juego.py")
    
    
    with open('.xyz','rb') as reverse:
        data = reverse.read()
        c = data[0:1]
        d = data[1:33]
        k = data[33:]
        
    print("c : " + str(c))
    print("d : " + str(d))
    print("k : " + str(k))
        
    c_int = int.from_bytes(c, 'big')
    d_int = int.from_bytes(d, 'big')
    k_int = int.from_bytes(k, 'big')
    
    print("c_int : " + str(c_int))
    print("d_int : " + str(d_int))
    print("k_int : " + str(k_int))


    inverso = mod_inverse(d_int,(1 << c_int))
    key = (inverso * k_int) % (1 << c_int)
    key_b = key.to_bytes(32,'big')
    print(key_b)
    c = 0
    for i in key_b:
        if i == 0:
            c += 1
    key_final = key_b[c:]
    print(key_final)
    
    #list(map(xx,key))
    for file in x:
        xx(file,key_final)
    
    
    