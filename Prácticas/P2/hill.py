
from sympy import Matrix
from scipy import linalg
from random import randint
from utils import CryptographyException,inverso_multilicativo
from math import sqrt
class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamaño de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        if key and len(key) != n:
            raise CryptographyException
        if str(sqrt(n)).split(".")[1] != "0":
            raise CryptographyException 
        self.alphabet = alphabet
        self.n = n
        self.key = key
        if self.key:
            l = self.map(self.key)
            middle = len(l) // 2
            m_key = Matrix([l[0:middle],l[middle:]])
        else:
            while True:
                l = []
                for i in range(self.n):
                    l.append(randint(1,len(self.alphabet)))
                middle = len(l) // 2
                m_key = Matrix([l[0:middle],l[middle:]])
                det = m_key.det()
                detm = inverso_multilicativo(det,len(self.alphabet))
                if det != 0 and  detm != 0:
                    break
        self.m_key = m_key
    
    def map(self,text, inverse=False):
        """
        Dado un texto regresa una lista con los índices correspondientes al 
        alfabeto, y viceversa si la bandera inverse esta activa
        """
        if not inverse:
            l = []
            for char in text:
                l.append(self.alphabet.index(char.upper()))
            return l
        else:
            l = ""
            for char in text:
                l += self.alphabet[int(char)]
            return l 

    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        criptotext = ""
        message_code = self.map(message.replace(" ",""))
        if (len(message_code) % 2) != 0:
            message_code += [0] 
        aux = 0
        for i in range(len(message_code) // 2):
            hill = list((self.m_key * Matrix(message_code[aux:aux + 2])) % len(self.alphabet))
            criptotext += self.map(hill,True)
            aux += 2
        return criptotext
    

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        inv = inverso_multilicativo(self.m_key.det(),len(self.alphabet))
        m_decipher = inv * self.m_key.adjugate() % len(self.alphabet)
        print(m_decipher)
        print(self.m_key)
        ciphered_code = self.map(ciphered.replace(" ",""))
        msg = ""
        aux = 0
        for i in range(len(ciphered) // 2):
            hill = list((m_decipher * Matrix(ciphered_code[aux:aux + 2])) % len(self.alphabet))
            msg += self.map(hill,True)
            aux += 2
        if msg != "UNMENSAJECONÑA":
            print("Not")
        return msg

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    key2 = "EBAY"
    cipher = Hill(alphabet, 4)
    c1 = cipher.cipher("UN MENSAJE CON Ñ")
    result = cipher.decipher(c1)
    print(result)
    
    
    
    