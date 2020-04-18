#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 9 feb. 2020

@author: felipe, marco
'''
from RC4 import rc4_encrypt


def bytes_to_int(bytes):
    aux = []
    for i in bytes:
        aux.append(i)
    return aux


if __name__ == "__main__":
    tarea_alicia = b"""No. de cuenta: 0123456789\nTarea 3\nRespuestas...
                    """
    print(tarea_alicia.decode("utf-8"))
    
    num_cta_carlos = b'1231231231'
    tarea_alicia_cifrada = rc4_encrypt(b'0123456789', tarea_alicia)    
    num_cta_carlos_int = bytes_to_int(num_cta_carlos)
    tarea_alicia_cifrada_int = bytes_to_int(tarea_alicia_cifrada)
    
    flujo_aleatorio = []
    for i in range(len(tarea_alicia_cifrada_int)):
        flujo_aleatorio.append(tarea_alicia[i] ^ tarea_alicia_cifrada_int[i])
    reemplazo = []
    
    c = 15
    for i in range(len(num_cta_carlos_int)):
        reemplazo.append(num_cta_carlos_int[i] ^ flujo_aleatorio[c])
        c += 1    
    tarea_alicia_cifrada_int[15:25] = reemplazo    
    
    decrypt = rc4_encrypt(b'0123456789', tarea_alicia_cifrada_int)
    print(decrypt.decode("utf-8"))
    
    
