from utils import euclides, CryptographyException, prime_relative

class Affine():
    
    def __init__(self, alphabet, A = None, B = None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet = alphabet
        A= A if A else 1
        if prime_relative(A,len(self.alphabet)):
            self.A = A
        else:
             raise (CryptographyException())
        self.B = B
        
    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        respuesta = ""
        for letra in message:
            # Por cada caracter del mensaje aplicamos la sustitución correspondiente
            respuesta += self.alphabet[((self.A * self.alphabet.index(letra)) + self.B) % (len(self.alphabet))]
        return respuesta
    
    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        respuesta = ""
        # Inverso multiplicativo de A
        inverso = euclides(self.A,len(self.alphabet))        
        for letra in criptotext:
            # La clave oara obetener el texto claro es tener el inverso multiplicativo
            respuesta += self.alphabet[((self.alphabet.index(letra) - self.B) * inverso ) % len(self.alphabet)]
        return respuesta

        
