from sympy import Matrix
from random import randint
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
        self.alphabet = alphabet
        self.n = n
        self.key = key


    def map (self,text):
        l = []
        for char in text:
           l.append(self.alphabet.index(char.upper()))
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
            m = Matrix.ones(self.n,self.n)
            m.row_insert(0,Matrix([l]))
        else:
            l = []
            for i in range(self.n):
                l.append(randint(0,self.n))

        
        print(m)




    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """

if __name__ == "__main__":
    hill = Hill("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",5,"abcde")
    #print(hill.map("hola"))
    hill.cipher("text")