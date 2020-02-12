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
        if key:
            self.key = key
        else:
            self.key = 1
        

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        res = ""
        # Si la bandera es None, entonces no tomamos en cuenta los espacios
        # al menos que sean parte del alfabeto
        if not flag :
            # Bandera auxiliar para saber si el caracter "espacio" es
            # parte del alfabeto
            if " " in self.alphabet:
                flag_aux = True
            else:
                flag_aux = False
            
            for c in message:
                # Si el mensaje contiene un espacio y no es parte del alfabeto
                if c == " " and not flag_aux:
                    # Lo ignoramos
                    pass
                else:
                    # En otro caso aplicamos la sustitución correspondiente
                    res += self.alphabet[(self.alphabet.index(c) + self.key) % len(self.alphabet)]
            
        # En otro caso dejamos los espacios en el mensaje
        else:
            for c in message:
                if c == " ":
                    res += " "
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

