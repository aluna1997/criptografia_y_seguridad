class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message
    
def inverso_multilicativo(a,m):
    for b in range(m):
        x=(a*b)%m
        if (x==1):
            return b
    return 0