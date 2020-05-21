from random import randint,choice
from scipy.constants.constants import pt
class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        if password:
            self.password = password
        else:
            self.password = ""
            rand = randint(4,len(self.alphabet))
            for i in range(rand):
                self.password += choice(self.alphabet)

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        pass_aux = ""
        for i in range(len(message)):
            pass_aux += self.password[i % len(self.password)]
        self.pass_aux = pass_aux
        
        criptotex = ""
        for j in range(len(message)):
            criptotex += self.alphabet[(self.alphabet.index(pass_aux[j]) + self.alphabet.index(message[j])) % len(self.alphabet)]
        return criptotex


    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        message = ""
        list_key = [self.alphabet.index(l) for l in self.pass_aux]
        list_msg = [self.alphabet.index(l) for l in list(ciphered)]
        for i in range(len(list_msg)):
            message += self.alphabet[(list_msg[i] - list_key[i]) % len(self.alphabet)]
        return message
                