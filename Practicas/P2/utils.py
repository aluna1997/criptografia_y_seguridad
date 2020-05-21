class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message
    
def inverso_multilicativo(num,len_alphabet):
    for i in range(len_alphabet):
        x = (num * i) % len_alphabet
        if (x == 1):
            return i
    return 0