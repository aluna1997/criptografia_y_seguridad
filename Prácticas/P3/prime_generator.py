from random import randint
from random import randrange
import math
import sys
sys.setrecursionlimit(1000000)

def fact_tail(n, a): 
    if (n == 0): 
        return a 
    return fact_tail(n - 1, n * a) 
  
def tail_factorial(n): 
    return fact_tail(n, 1) 


def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    aux = ""
    if not size or size < 100:
        size = randint(100,150)
    for i in range(size):
        aux += str(randint(0,9))
    return int(aux)


def check(a,s,d,n):
    x = pow(a,d,n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == 1:
            return True
        for i in range(s - 1):
            if x == (n - 1):
                return True
            x = pow(x,2,n)
        return x == (n - 1)

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    k = 512
    r = n - 1
    s = 0
    a = 0
    while (r % 2 == 0): 
        r = r >> 1 
        s += 1
    for i in range(k):
        if (n - 2) > 2:
            a = randint(2,n - 2)
        else:
            a = randint(n - 2, 2)
        y = pow(a,r,n)
        if y != 1 and y != (n - 1):
            j = 1
            while j <= (s - 1) and y != (n - 1):
                y = pow(y,2,n)
                if y == 1:
                    return False
                j += 1
            if y != (n - 1):
                return False
    return True            

def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    r = tail_factorial(n - 1) + 1 
    v = r % n
    if (v == 0):
        return True
    else:
        return False
    
if __name__ == "__main__":
    #print(wilson(11))
    for i in open("primes.txt","r").readlines():
        print(wilson(int(i)))


