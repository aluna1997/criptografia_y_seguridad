from sympy.crypto.crypto import encipher_shift, decipher_shift


class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        self.key = key
        

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        res = ''
        for c in message:
            if flag:
                if c == " ":
                    res += " "
                else:
                    res += self.alphabet[(self.alphabet.index(c) + self.key) % len(self.alphabet)]
            else:
                res += self.alphabet[(self.alphabet.index(c) + self.key) % len(self.alphabet)]
        return res

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        obj = Caesar(self.alphabet,-self.key)
        return obj.cipher(criptotext, flag)


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    c1 = Caesar(alphabet, 1)
    print(c1.cipher("UNMENSAJECONÑ"))
    print(c1.decipher("VÑNFÑTBKFDPÑO"))

