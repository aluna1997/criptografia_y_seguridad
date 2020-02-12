class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)
    
def euclides(a, b):
    """
    Algoritmo extendido de Euclides
    Parámetro:
            a -- número entero a aplicar el algoritmo
            b -- número entero a aplicar el algoritmo
    """
    for y in range(b):
        x = (a * y) % b
        if x == 1:
            return y
    return 0
