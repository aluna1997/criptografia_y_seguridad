
def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """ 
    result = ''
    for i in message:
        result += chr(ord(i) ^ 1).encode().decode("utf-8") 
    return result
    
def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    return cipher(criptotext)

if __name__ == "__main__":
    print(cipher("Do not spill the beans"))
    print(decipher("Do not spill the beans"))

