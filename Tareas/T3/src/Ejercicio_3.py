#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 9 feb. 2020

@author: felipe, marco
'''
import array
from RC4 import rc4_encrypt

if __name__ == "__main__":
    tarea_alicia = b"""No. de cuenta: 313204567
                      Tarea 3
                      Respuestas...
                    """
    tarea_alicia_cifrada = rc4_encrypt(b'anitalavalatina',tarea_alicia)
    tarea_alicia_cifrada_hex = tarea_alicia_cifrada.hex()
    #print(tarea_alicia_cifrada_hex)
    num_cta_carlos = b'313203079'
    key_stream = tarea_alicia_cifrada[15:24]
    
    #print(key_stream.hex())
    reemplazo = []
    for i in range(9):
        reemplazo.append(num_cta_carlos[i] ^ key_stream[i])
    
    reemplazo = array.array('B',reemplazo).tostring()
    
    tarea_alicia_cifrada = bytearray(tarea_alicia_cifrada)
    reemplazo = bytearray(reemplazo)

    tarea_alicia_cifrada[15:24] = reemplazo
    
    decrypted = rc4_encrypt(b'anitalavalatina', tarea_alicia_cifrada)
    print(decrypted)
    
    
    
    
    




    
    
    
    
    