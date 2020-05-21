from random import randint
def prime_relative(a, b):
    if(b == 0):
        return a == 1
    else:
        return prime_relative(b, a%b)

def elige_e(phi):
    e = randint(1,phi)
    while not prime_relative(e, phi):
        e = randint(1,phi)
    return e

if __name__ == "__main__":
    print(prime_relative(11, 12))
    print(elige_e(12)) 