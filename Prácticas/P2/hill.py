
from sympy import Matrix
from random import randint
from utils import CryptographyException
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


    def map(self,text, inverse=False):
        if not inverse:
            l = []
            for char in text:
                l.append(self.alphabet.index(char.upper()))
            return l
        else:
            l = []
            for char in text:
                l.append(self.alphabet[int(char)])
            return l 

    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        if self.key:
            l = self.map(self.key)
            if len(l) != self.n:
                for i in range(self.n - len(l)):
                    l.append(randint(0,self.n))
            m_ones = Matrix.ones(self.n - 1,self.n)
            m_key = m_ones.row_insert(0,Matrix([l]))
        else:
            l2 = []
            for i in range(self.n):
                l = []
                for j in range(self.n):
                    l.append(randint(0,self.n))
                l2.append(l)
                
            m_key = Matrix(l2)
        
        m_message = Matrix(self.map(message))
        m_hill = (m_key * m_message) % len(self.alphabet)
        print (list(m_hill))    
        return self.map(list(m_hill),True) 



    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """

if __name__ == "__main__":
    hill = Hill("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",4,"hola")
    print(hill.cipher("text"))