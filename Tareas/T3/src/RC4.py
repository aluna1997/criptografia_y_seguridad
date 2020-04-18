#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 9 feb. 2020

@author: felipe, marco
'''


def rc4_encrypt(key, data):
    # Inicialización
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256
        box[i], box[x] = box[x], box[i]
        
    # Generación de bytes pseudoaleatorios y cifrado
    x = 0
    y = 0
    out = []
    for byte in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(byte ^ box[(box[x] + box[y]) % 256])
    return bytes(out)



    

if __name__ == "__main__":
    #print(rc4_encrypt(b'Key', b'Plaintext').hex())
    #bbf316e8d940af0ad3
    #print(rc4_encrypt(b'Wiki', b'pedia').hex())
    #1021bf0420
    #print(rc4_encrypt(b'Secret', b'Attack at dawn').hex())
    #45a01f645fc35b383552544b9bf5
    plain = b'this is plaintext 313203079'
    key = b'Hola 111111111'

    # testing encryption
    encrypted = rc4_encrypt(key, plain)
    print('encrypted: ' + str(encrypted))
    print(type(encrypted))

    # testing decryption
    decrypted = rc4_encrypt(key, encrypted)
    print('decrypted: ' + str(decrypted))
    print(type(decrypted))


